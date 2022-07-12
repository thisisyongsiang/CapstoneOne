import MergeSort
import Heapsort
import QuickSelect
import json
import time

# Get and Sort Results from Yelp API
dir="yelpAPIData.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

# QuickSelect
start_time = time.time()
firstN = QuickSelect.getFirstN(data, 'distance', 5, False)
print("QuickSelect - Time taken = {:.20f} seconds".format(time.time() - start_time))

# MergeSort
start_time = time.time()
firstN = MergeSort.getFirstN(data, 'distance', 5, False)
print("MergeSort - Time taken = {:.20f} seconds".format(time.time() - start_time))

# HeapSort
start_time = time.time()
firstN = Heapsort.getItemsByField(data, 'distance', False).getTopN(5)
print("HeapSort - Time taken = {:.20f} seconds".format(time.time() - start_time))
