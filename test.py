import json
import time

import MergeSort
import QuickSelect
import Heapsort
import CategoryAndFilter

dir="yelpAPIDataMerged.json"
f=open(dir,encoding='utf-8')
data=json.load(f)

simpleData=CategoryAndFilter.simplifyData(data,[1.2878106890101897, 103.83402793907551
])
cat=CategoryAndFilter.getCategories(simpleData,[])
Heapsort.getFirstN(cat['american (traditional)'],'recommendation',5,True)
# start=time.time()
# firstN=MergeSort.getFirstN(data,'review_count',10,False)
# end=time.time()
# [print(c['name'],c['review_count']) for c in firstN]
# print("mergesort time taken = {0}".format(end-start) )

# f=open(dir,encoding='utf-8')
# data=json.load(f)
# start=time.time()
# firstN=QuickSelect.getFirstN(data,'review_count',10,False)
# end=time.time()
# [print(c['name'],c['review_count']) for c in firstN]
# print("quickSelect time taken = {0}".format(end-start) )