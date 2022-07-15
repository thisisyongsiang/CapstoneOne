import MergeSort
import Heapsort
import QuickSelect
import json
import time
import CategoryAndFilter as caf

# Get and Sort Results from Yelp API
dir="singaporeFnBAll.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

dataqs = caf.simplifyData(data, [1.397427, 103.881539], 1, 1, 1)

# # QuickSelect
start_time = time.time()
qs=QuickSelect.QuickSelect(dataqs, 'distance', True)
firstN =qs.GetNextN(5)
end_time=time.time()
print("QuickSelect - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =qs.GetNextN(5)
end_time=time.time()
print("QuickSelect next 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =qs.GetNextN(5)
end_time=time.time()
print("QuickSelect next 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =qs.GetPrevN(5)
end_time=time.time()
print("QuickSelect prev 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

#############################################################################################
# MergeSort
datams = caf.simplifyData(data, [1.397427, 103.881539], 1, 1, 1)

start_time = time.time()
ms=MergeSort.MergeSort(datams, 'distance', True)
firstN =ms.GetNextN(5)
end_time=time.time()
print("MergeSort - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =ms.GetNextN(5)
end_time=time.time()
print("MergeSort next 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =ms.GetNextN(5)
end_time=time.time()
print("MergeSort next 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =ms.GetPrevN(5)
end_time=time.time()
print("MergeSort prev 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()
#############################################################################################

# HeapSort
datahs = caf.simplifyData(data, [1.397427, 103.881539], 1, 1, 1)

start_time = time.time()
hs=Heapsort.getItemsByField(datahs, 'distance', True)
firstN = hs.getNextN(5)
end_time=time.time()
print("HeapSort - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()
start_time = time.time()
firstN =hs.getNextN(5)
end_time=time.time()
print("HeapSort next 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =hs.getNextN(5)
end_time=time.time()
print("HeapSort next 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
print()

start_time = time.time()
firstN =hs.getPrevN(5)
end_time=time.time()
print("HeapSort prev 5 - Time taken = {:.20f} seconds".format(end_time - start_time))
[print(c['name'],c['distance']) for c in firstN]
#############################################################################################