import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import folium
import MergeSort
import CategoryAndFilter as ct
import Heapsort
import csv


# Title
st.write("""
# Food Recommender App
""")
st.subheader("")
st.subheader("Top Restaurants")

# Generate Containers
results_container = st.container()


# Initialise session state counters
if 'get_next' not in st.session_state:
    st.session_state.get_next = False

if 'get_prev' not in st.session_state:
    st.session_state.get_prev = False

if 'load_ctr' not in st.session_state:
    st.session_state.load_ctr = 0

if 'current_sort' not in st.session_state:
    st.session_state.current_sort = "Recommendation"
if 'sort_by' not in st.session_state:
    st.session_state.sort_by = "Recommendation"

def showResults(topN):
    # Display Results Table and Map
    df = pd.DataFrame(topN)
    if not df.empty:
        with results_container:
            df = df[["name", "distance", "recommendation", "display_price", "category"]]
            df["distance"] = df["distance"].astype(int)
            df["recommendation"] = df["recommendation"].round(2).astype(str)
            df.rename(columns = {"name":"NAME", "distance":"DISTANCE(m)", "recommendation": "RECOMMENDATION", "display_price":"PRICE", "category":"CATEGORIES"}, inplace=True)
            hide_table_row_index = """
                    <style>
                    tbody th {display:none}                
                    .blank {display:none}
                    </style>
            """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(df)
        
            map_sg = folium.Map(location=st.session_state.center, zoom_start=13)
            folium.Marker(st.session_state.center, popup = "You are here!", icon=folium.Icon(color="red")).add_to(map_sg)

            for row in topN:
                location = [row["latitude"], row["longitude"]]
                folium.Marker(location, popup = folium.Popup("<b>{}</b><br>{}".format(row["name"], row["address"]), max_width=300), tooltip=row["name"]).add_to(map_sg)

            map_sg.save("map.html")
            map = open("map.html")
            components.html(html=map.read(), width=750, height=500, scrolling=True)

            #st.write(len(st.session_state.sorted_data.arr))  # TODO REMOVE
            #st.write(len(st.session_state.clean_data))  # TODO REMOVE
    else:
        results_container.write("!!! No restaurants matched your criteria. Please adjust your filters or you have reached the end of the list. !!!")

sort_by = st.radio("Sort results by: ", ("Recommendation", "Distance", "Price"), key="selected_filter_visited")
st.session_state.sort_by = sort_by

st.subheader("")

col1, buff, col2 = st.columns([1,5,1])
with col1:
    if st.button("Prev 5"):
        st.session_state.get_prev = True
        st.session_state.get_next = False

with col2:
    if st.button("Next 5"):
        st.session_state.get_prev = False
        st.session_state.get_next = True

# st.session_state  # TODO REMOVE

if st.session_state.load_ctr == 0:
    # Get Results from Yelp API
    dir="singaporeFnBAll.json"
    f=open(dir,encoding='utf-8')
    st.session_state.data=json.load(f)

    # Get Food Categories
    categories = ct.getCategories(st.session_state.data)
    categories.sort()

    st.session_state.sorted_categories = categories
    st.session_state.load_ctr += 1

# User Input Form
st.sidebar.header("User Inputs")

with st.sidebar.form("my-form"):
    selected_location = st.text_input("Lat/Long", "", key="selected_location")
    selected_food_category = st.selectbox("Food Category", st.session_state.sorted_categories, key="selected_category")
    weightage = st.multiselect("Select preferences in order of priority: ", ["Distance", "Price", "Rating"], key="selected_weightage")
    range_distance = st.slider(
        'Distance Range',
        0, 10000, (0, 10000), step=100, key="selected_range_distance")

    range_price = st.slider(
        'Price Range',
        1, 4, (1, 4), step=1, key="selected_range_price")

    ignore_price = st.checkbox("Ignore Price Filter? (some places have missing price rating)", key="selected_ignore_price")

    filter_visited = st.radio("Remove previously visited places?", ("No", "Yes"), key="selected_filter_visited")

    submitted = st.form_submit_button("Show Results!")


# Generate Recommendations after User Submits Inputs
if submitted:
    # Reset States
    if 'sorted_data' in st.session_state:
        del st.session_state.sorted_data
    if 'clean_data' in st.session_state:
        del st.session_state.clean_data
    if 'center' in st.session_state:
        del st.session_state.center
    st.session_state.get_prev = False
    st.session_state.get_next = False


    # Recalculate Distances and Filter Data
    values = selected_location.split(',')
    st.session_state.center = [float(values[0]), float(values[1])]

    clean_data = ct.simplifyData(st.session_state.data, st.session_state.center, weightage.index("Rating") + 1, weightage.index("Price") + 1, weightage.index("Distance") + 1)
    clean_data = ct.getMultipleFoodCategories(clean_data, [selected_food_category])

    if not ignore_price:
        clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'price', [range_price[0],range_price[1]])

    clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'distance', [range_distance[0],range_distance[1]])

    if filter_visited == "Yes":
        visited = []
        with open("visited.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                visited.append(row[0])

        clean_data = ct.filterVisited(clean_data, visited)

    places = [row['name'] for row in clean_data]
    places.sort()

    st.session_state.clean_data = clean_data

    # Output Results
    st.session_state.sorted_data = Heapsort.getItemsByField(st.session_state.clean_data, "recommendation", False)

    top_n = st.session_state.sorted_data.getNextN(5)
    showResults(top_n)

    st.subheader("")


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
    if st.session_state.current_sort != st.session_state.sort_by:
        st.session_state.current_sort = st.session_state.sort_by
        sort = st.session_state.sort_by.lower()
        if sort == "recommendation":
            st.session_state.sorted_data = Heapsort.getItemsByField(st.session_state.clean_data, st.session_state.sort_by.lower(), False)
        else:
            st.session_state.sorted_data = Heapsort.getItemsByField(st.session_state.clean_data, st.session_state.sort_by.lower(), True)
        showResults(st.session_state.sorted_data.getNextN(5))

        st.write(len(st.session_state.sorted_data.arr))     # TODO REMOVE
        st.write(len(st.session_state.clean_data))

    elif st.session_state.get_next and not st.session_state.get_prev:
        showResults(st.session_state.sorted_data.getNextN(5))
    elif st.session_state.get_prev and not st.session_state.get_next:
        showResults(st.session_state.sorted_data.getPrevN(5))
    else:
        st.write("<<< Select your preferencs and click 'Show Results!' to get your top recommended restaurants! <<<")