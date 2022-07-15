import json
import time

from numpy import full

import MergeSort
import QuickSelect
import Heapsort
import CategoryAndFilter as ct
import streamlit as st

dir="/Users/robertsalomone/Downloads/singaporeFnBAll_final2.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

simpleData=ct.simplifyData(data,[1.2872977, 103.8339319
],3,1,2)
clean_data = ct.getMultipleFoodCategories(simpleData, ['italian restaurant'])
clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'price', [3,4])
clean_data = ct.filterDataByFieldAndValueRange(clean_data, 'distance', [6000,10000])

full_sorted_data = Heapsort.getItemsByField(clean_data, "recommendation", False)
print(len(clean_data))

# st.session_state.clean_data = clean_data
# sesh_state_clean_data = st.session_state.clean_data
# st.session_state.full_sorted_data = Heapsort.getItemsByField(sesh_state_clean_data, "recommendation", False)


# top_n = full_sorted_data.getNextN(5)

next_output = []
prev_output = []
for i in range(len(clean_data)//5+1):
    top_n = full_sorted_data.getNextN(5)
    print("loop {}".format(i))
    print([top_n[i]['name'] for i in range(len(top_n))])

    if i > len(clean_data)//5-4 and i < len(clean_data):
        next_output += [top_n[i]['name'] for i in range(len(top_n))]

for i in range(3):
    prev_n = full_sorted_data.getPrevN(5)
    print("loop {}".format(i))
    print([prev_n[i]['name'] for i in range(len(prev_n))])
    prev_output += [prev_n[i]['name'] for i in range(len(prev_n))]

discrep = False
for i in range(len(prev_output)):
    if prev_output[i] not in next_output:
        print("DISCREP")
        discrep = True

if not discrep:
    print("ALL GOOD")


# print("top 5")
# print([top_n[i]['name'] for i in range(len(top_n))])

# top_n2 = full_sorted_data.getNextN(5)
# print("next 5")
# print([top_n2[i]['name'] for i in range(len(top_n2))])

# prev_n = full_sorted_data.getPrevN(5)
# print("prev5")
# print([prev_n[i]['name'] for i in range(len(prev_n))])


# session_top_n = st.session_state.full_sorted_data.getNextN(5)
# session_top_n2 = st.session_state.full_sorted_data.getNextN(5)
# session_prev_n = st.session_state.full_sorted_data.getPrevN(5)

# print("top 5 with session state")
# print([session_top_n[i]['name'] for i in range(len(session_top_n))])
# print("next 5 with session state")
# print([session_top_n2[i]['name'] for i in range(len(session_top_n2))])
# print("prev 5 with session state")
# print([session_prev_n[i]['name'] for i in range(len(session_prev_n))])