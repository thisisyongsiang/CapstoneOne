from numpy import sort_complex
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import folium
import MergeSort
import CategoryAndFilter as ct
import Heapsort


st.write("""
# Food Recommender

### Random restaurant picker!

""")

# Get Results from Yelp API
dir="yelpAPIData.json"
f=open(dir,encoding='utf-8')
data=json.load(f)


# Get Food Categories
unwanted = ["arts & entertainment", "bikes", "butcher", "candy stores", "car wash", "caterers", "convenience stores", "department stores", "discount store", "do-it-yourself food", "electronics", "food", "food delivery services", "gas stations", "henghwa", "home services", "imported food", "international grocery", "internet cafes", "meat shops", "nutritionists", "restaurants", "seafood markets", "shopping", "venue & event spaces", "wholesale stores"]
categories = [*ct.getCategories(data)]
categories_clean = [i for i in categories if i not in unwanted]
categories_clean.sort()

# User Input
st.sidebar.header("User Inputs")

selected_location = st.sidebar.text_input("Lat/Long", "")
selected_food_category = st.sidebar.selectbox("Food Category", categories_clean)

range_distance = st.sidebar.slider(
     'Distance Range',
     0, 10000, (0, 10000), step=100)

range_price = st.sidebar.slider(
     'Price Range',
     1, 5, (1, 5), step=1)


# Output Results
st.subheader("Top 5 Recommended Restaurants based on your selection")

<<<<<<< HEAD
print(len(data))

#Mergesort
=======
>>>>>>> Add range sliders for distance and price selection and updated user input sidebar
# if selected_filter_category == "Distance":
#     lst = MergeSort.getFirstN(data, "distance", 5, False)
# elif selected_filter_category == "Rating/Review":           # TODO: Filter categories to discuss. Not all json objects has 'Price' 
#     lst = MergeSort.getFirstN(data, "rating", 5, False)

<<<<<<< HEAD
#Heapsort
bizData = pd.DataFrame()
print(data[0])
for i in range(len(data)):

    newDict = {x: data[i][x] for x in ['id', 'name', 'rating', 'price', 'distance', 'review_count'] if x in data[i].keys()}
    bizData = bizData.append(newDict, ignore_index=True)

print(bizData)

if selected_filter_category == "Distance":
    lst = Heapsort.heapSortByDistance(bizData, 5)
elif selected_filter_category == "Rating/Review":           # TODO: Filter categories to discuss. Not all json objects has 'Price' 
    lst = Heapsort.heapSortByReview(bizData, 5)

print(lst)
=======
lst = MergeSort.getFirstN(data, "distance", 5, False)
>>>>>>> Add range sliders for distance and price selection and updated user input sidebar

df = pd.DataFrame(lst)
df = df[["name", "distance", "rating", "review_count"]]
df.rename(columns = {"name":"Name", "distance":"Distance(m)", "rating":"Rating", "review_count":"Reviews"}, inplace=True)
df = df.style.hide_index()
st.write(df.to_html(), unsafe_allow_html=True)

st.write("User Location: {}".format(selected_location))
st.write("Selected Food Category: {}".format(selected_food_category))


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