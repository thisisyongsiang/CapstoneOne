import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import folium
import MergeSort
import CategoryAndFilter as ct


st.write("""
# Food Recommender

### Random restaurant picker!

""")

# Get and Sort Results from Yelp API
dir="yelpAPIData.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

categories = ct.getCategories(data)


# User Input
st.sidebar.header("User Inputs")

selected_location = st.sidebar.text_input("Lat/Long", "")
selected_food_category = st.sidebar.selectbox("Food Category", categories)

filter_categories = ["Distance", "Rating/Review", "Price"]
selected_filter_category = st.sidebar.selectbox("Filter Category", filter_categories)

# Output Results
st.subheader("Here are the Top 5 restaurants based on your selection")

if selected_filter_category == "Distance":
    lst = MergeSort.getFirstN(data, "distance", 5, False)
elif selected_filter_category == "Rating/Review":           # TODO: Filter categories to discuss. Not all json objects has 'Price' 
    lst = MergeSort.getFirstN(data, "rating", 5, False)

df = pd.DataFrame(lst)
df = df[["name", "distance", "rating", "review_count"]]
df.rename(columns = {"name":"Name", "distance":"Distance(m)", "rating":"Rating", "review_count":"Reviews"}, inplace=True)
df = df.style.hide_index()
st.write(df.to_html(), unsafe_allow_html=True)

st.write("User Location: {}".format(selected_location))
st.write("Selected Food Category: {}".format(selected_food_category))
st.write("Selected Filter Category: {}".format(selected_filter_category))


# Generate Map
center = [1.35644, 103.83297]   # User Location
map_kenya = folium.Map(location=center, zoom_start=13)
folium.Marker(center, popup = "You are here!", icon=folium.Icon(color="red")).add_to(map_kenya)

# Add locations to map
for row in lst:
    print(row["coordinates"])
    location = [row["coordinates"]["latitude"], row["coordinates"]["longitude"]]
    folium.Marker(location, popup = folium.Popup("<b>{}</b><br>{}".format(row["name"], row["location"]["display_address"]), max_width=300), tooltip=row["name"]).add_to(map_kenya)

map_kenya.save("map.html")
map = open("map.html")
components.html(html=map.read(), width=750, height=500, scrolling=True)