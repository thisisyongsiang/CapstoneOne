from numpy import sort_complex
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import folium
import MergeSort
import CategoryAndFilter as ct
import Heapsort
import math


st.write("""
# Food Recommender

### Random restaurant picker!

""")

# Get Results from Yelp API
dir="yelpAPIDataMerged.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

# Get Base Data to display first
clean_data = ct.simplifyData(data)

# Get Food Categories
unwanted = ["art galleries", "arts & entertainment", "bikes", "butcher", "candy stores", "car wash", "caterers", "convenience stores", "department stores", "discount store", "do-it-yourself food", "electronics", "food", "food delivery services", "gas stations", "henghwa", "home services", "imported food", "international grocery", "internet cafes", "meat shops", "nutritionists", "restaurants", "seafood markets", "shopping", "venue & event spaces", "wholesale stores"]
categories = ct.getCategories(clean_data)
categories_clean = [i for i in categories if i not in unwanted]
categories_clean.sort()


# User Input
st.sidebar.header("User Inputs")

center = [1.35644, 103.83297]   # User Location
selected_location = st.sidebar.text_input("Lat/Long", "")

selected_food_category = st.sidebar.selectbox("Food Category", categories_clean)

range_distance = st.sidebar.slider(
     'Distance Range',
     0, 10000, (0, 10000), step=100)

range_price = st.sidebar.slider(
     'Price Range',
     1, 5, (1, 5), step=1)


# Get User Input filtered data if Location is input
if (selected_location != ""):
    values = selected_location.split(',')
    latlong = [float(values[0]), float(values[1])]
    clean_data = ct.simplifyData(data, latlong)
    center = latlong

    print("Clean Data 1: ", len(clean_data))
    print("Filter cat: ", selected_food_category)
    clean_data = ct.getMultipleFoodCategories(clean_data, [selected_food_category])
    print("Clean Data 2: ", len(clean_data))




# Output Results
st.subheader("Top 5 Recommended Restaurants based on your selection")

lst = Heapsort.getFirstN(clean_data, "recommendation", 5, False)
df = pd.DataFrame(lst)
df = df[["name", "distance", "rating", "review_count", "recommendation", "display_price", "category"]]
df.rename(columns = {"name":"Name", "distance":"Distance(m)", "rating":"Rating", "review_count":"Reviews", "recommendation": "Recommendation", "display_price":"Price"}, inplace=True)
df = df.style.hide_index()
st.write(df.to_html(), unsafe_allow_html=True)

st.write("User Location: {}".format(selected_location))
st.write("Selected Food Category: {}".format(selected_food_category))


# Generate Map
map_kenya = folium.Map(location=center, zoom_start=13)
folium.Marker(center, popup = "You are here!", icon=folium.Icon(color="red")).add_to(map_kenya)

# Add locations to map
for row in lst:
    location = [row["coordinates"]["latitude"], row["coordinates"]["longitude"]]
    folium.Marker(location, popup = folium.Popup("<b>{}</b><br>{}".format(row["name"], row["location"]["display_address"]), max_width=300), tooltip=row["name"]).add_to(map_kenya)

map_kenya.save("map.html")
map = open("map.html")
components.html(html=map.read(), width=750, height=500, scrolling=True)