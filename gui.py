import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import folium
import MergeSort
import CategoryAndFilter as ct
import Heapsort
import math
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events


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

button_press = False
latlonginput = ""

with st.sidebar.container():
    loc_button = Button()
    loc_button.js_on_event("button_click", CustomJS(code="""
        navigator.geolocation.getCurrentPosition(
            (loc) => {
                document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
            }
        )
        """))
    result = streamlit_bokeh_events(
        loc_button,
        events="GET_LOCATION",
        key="get_location",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0)

    selected_location = st.sidebar.text_input("Lat/Long", latlonginput)

    if result:
        latlonginput = latlonginput + str(result['GET_LOCATION']['lat']) + ", " + str(result['GET_LOCATION']['lon'])
        print(latlonginput)
        st.write(latlonginput)
        selected_location = latlonginput


selected_food_category = st.sidebar.selectbox("Food Category", categories_clean)

range_distance = st.sidebar.slider(
     'Distance Range',
     0, 10000, (0, 10000), step=100)

range_price = st.sidebar.slider(
     'Price Range',
     0, 5, (0, 5), step=1)

filter_visited = st.sidebar.radio("Remove previously visited places?", ("No", "Yes"))

# Get User Input filtered data if Location is input
if (selected_location != ""):
    values = selected_location.split(',')
    latlong = [float(values[0]), float(values[1])]
    clean_data = ct.simplifyData(data, latlong)
    center = latlong

    print("Clean Data 1: ", len(clean_data))
    clean_data = ct.getMultipleFoodCategories(clean_data, [selected_food_category])
    clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'price', [range_price[0],range_price[1]])
    clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'distance', [range_distance[0],range_distance[1]])
    print("Clean Data 2: ", len(clean_data))

    if (filter_visited == "Yes"):
        df_visited = pd.read_csv("visited.csv", delimiter=',')
        visited = list(df_visited.columns.values)
        clean_data = ct.filterVisited(clean_data, visited)

    print("Clean Data 3: ", len(clean_data))

# Output Results
st.subheader("Top 5 Recommended Restaurants based on your selection")

lst = Heapsort.getFirstN(clean_data, "recommendation", 5, False)

df = pd.DataFrame(lst)

if not df.empty:
    df = df[["name", "distance", "rating", "review_count", "recommendation", "display_price", "category"]]
    df.rename(columns = {"name":"Name", "distance":"Distance(m)", "rating":"Rating", "review_count":"Reviews", "recommendation": "Recommendation", "display_price":"Price"}, inplace=True)
    df = df.style.hide_index()
    st.write(df.to_html(), unsafe_allow_html=True)
else:
    st.write("!!! No restaurants matched your criteria. Please adjust your filters. !!!")

st.subheader("")

# Generate Map
map_sg = folium.Map(location=center, zoom_start=13)
folium.Marker(center, popup = "You are here!", icon=folium.Icon(color="red")).add_to(map_sg)

# Add locations to map
for row in lst:
    location = [row["coordinates"]["latitude"], row["coordinates"]["longitude"]]
    folium.Marker(location, popup = folium.Popup("<b>{}</b><br>{}".format(row["name"], row["location"]["display_address"]), max_width=300), tooltip=row["name"]).add_to(map_sg)

map_sg.save("map.html")
map = open("map.html")

components.html(html=map.read(), width=750, height=500, scrolling=True)


#Alternative method to retrieve user location

# html_location = """
#     <html>
#     <body>

#         <p>Click the button to get your coordinates.</p>

#             <button onclick="getLocation()">Try It</button>

#         <p id="demo"></p>

#         <script>
#         var x = document.getElementById("demo");

#         function getLocation() {
#         if (navigator.geolocation) {
#             navigator.geolocation.getCurrentPosition(showPosition);
#         } else { 
#             x.innerHTML = "Geolocation is not supported by this browser.";
#         }
#         }

#         function showPosition(position) {
#         x.innerHTML = "Latitude: " + position.coords.latitude + 
#         "<br>Longitude: " + position.coords.longitude;
#         }
#     </script>

#     </body>
#     </html>
#     """

# components.html(html_location, width=250, height=250)