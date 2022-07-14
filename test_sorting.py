import MergeSort
import Heapsort
import QuickSelect
import json
import time
import CategoryAndFilter as caf

# Get and Sort Results from Yelp API
dir="/Users/robertsalomone/Downloads/singaporeFnBAll_final2.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

data = caf.simplifyData(data, [1.397427, 103.881539], 1, 1, 1)

# # QuickSelect
start_time = time.time()
firstN = QuickSelect.QuickSelect(data, 'distance', False).GetNextN(5)
print("QuickSelect - Time taken = {:.20f} seconds".format(time.time() - start_time))

# MergeSort
start_time = time.time()
firstN = MergeSort.MergeSort(data, 'popularity', False).GetNextN(5)
print("MergeSort - Time taken = {:.20f} seconds".format(time.time() - start_time))

# HeapSort
start_time = time.time()
firstN = Heapsort.getItemsByField(data, 'distance', False).getNextN(5)
print("HeapSort - Time taken = {:.20f} seconds".format(time.time() - start_time))
