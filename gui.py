import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import folium
import MergeSort
import CategoryAndFilter as ct
import Heapsort
import csv


st.write("""
# Food Recommender
""")
st.subheader("")
st.subheader("Top Recommended Restaurants")

# Get Results from Yelp API
dir="singaporeFnBAll.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

# Get Food Categories
categories = ct.getCategories(data)
categories.sort()


# User Input Form
st.sidebar.header("User Inputs")

with st.sidebar.form("my-form"):
    selected_location = st.text_input("Lat/Long", "", key="selected_location")
    selected_food_category = st.selectbox("Food Category", categories, key="selected_category")
    weightage = st.multiselect("Select preferences in order of priority: ", ["Distance", "Price", "Rating"], key="selected_weightage")
    range_distance = st.slider(
        'Distance Range',
        0, 10000, (0, 10000), step=100, key="selected_range_distance")

    range_price = st.slider(
        'Price Range',
        0, 5, (0, 5), step=1, key="selected_range_price")

    filter_visited = st.radio("Remove previously visited places?", ("No", "Yes"), key="selected_filter_visited")

    submitted = st.form_submit_button("Show Results!")


# Generate Recommendations after User Submits Inputs
if submitted:
    values = selected_location.split(',')
    latlong = [float(values[0]), float(values[1])]
    clean_data = ct.simplifyData(data, latlong,1,2,3)
    center = latlong

    clean_data = ct.getMultipleFoodCategories(clean_data, [selected_food_category])
    clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'price', [range_price[0],range_price[1]])
    clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'distance', [range_distance[0],range_distance[1]])

    if (filter_visited == "Yes"):
        visited = []
        with open("visited.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                visited.append(row[0])

        clean_data = ct.filterVisited(clean_data, visited)
    
    
    places = [row['name'] for row in clean_data]
    places.sort()

    # Output Results
    full_sorted_data = Heapsort.getItemsByField(clean_data, "recommendation", False)

    st.session_state.data = full_sorted_data     # Save sorted data object in key 'data'

    top_n = full_sorted_data.getTopN(5)
    df = pd.DataFrame(top_n)
    if not df.empty:
        df = df[["name", "distance", "rating", "review_count", "recommendation", "display_price", "category"]]
        df["distance"] = df["distance"].astype(int)
        df["rating"] = df["rating"].round(2).astype(str)
        df["recommendation"] = df["recommendation"].round(2).astype(str)
        df.rename(columns = {"name":"Name", "distance":"Distance(m)", "rating":"Rating", "review_count":"Reviews", "recommendation": "Recommendation", "display_price":"Price"}, inplace=True)
        df = df.style.hide(axis="index") 
        st.write(df.to_html(), unsafe_allow_html=True)
    else:
        st.write("!!! No restaurants matched your criteria. Please adjust your filters. !!!")

    st.subheader("")

    # Generate Map
    map_sg = folium.Map(location=center, zoom_start=13)
    folium.Marker(center, popup = "You are here!", icon=folium.Icon(color="red")).add_to(map_sg)

    for row in top_n:
        location = [row["coordinates"]["latitude"], row["coordinates"]["longitude"]]
        folium.Marker(location, popup = folium.Popup("<b>{}</b><br>{}".format(row["name"], row["location"]["display_address"]), max_width=300), tooltip=row["name"]).add_to(map_sg)

    map_sg.save("map.html")
    map = open("map.html")
    components.html(html=map.read(), width=750, height=500, scrolling=True)


    # Other Features
    st.sidebar.subheader("")
    st.sidebar.header("Other Features")

    selected_visited = st.sidebar.selectbox("Select restaurant to add to list of visited places", places)
    result = st.sidebar.button("Add Restaurant")

    if result:
        visited_places = []
        with open("visited.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                visited_places.append(row[0])

        if selected_visited not in visited_places:
            visited_places.append(selected_visited)
            with open("visited.csv", mode="w") as g:
                g.write("\n".join(visited_places))

else:
    st.write("<<< Select your preferencs and click 'Show Results!' to get your top recommended restaurants! <<<")