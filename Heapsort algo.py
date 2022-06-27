#Heapsort algo

from imghdr import tests
from matplotlib.pyplot import axis
import pandas as pd
import heapq

def heapSortByDistance(bizData, topX):
    ''' takes in Pandas dataframe with distance and id field and sorts via heapsort
    returns a sorted dataframe'''

    heap_dict = []

    for i in range(len(bizData.index)):
        heap_dict.append((bizData['distance'][i],bizData['id'][i]))

    heapq.heapify(heap_dict)

    outputDf = pd.DataFrame()
    sortedList = []

    for i in range(topX):
        sortedList.append(heapq.heappop(heap_dict))
    
    outputDf = pd.DataFrame(sortedList, columns=['distance','id'])
    outputDf2 = pd.merge(outputDf, bizData, on='id', how='left')
    outputDf2 = outputDf2.drop(['distance_y'], axis=1)
    outputDf2.rename(columns={'distance_x':'distance'}, inplace=True)
    
    return outputDf2

testData = {
    'id': ['test1','t2]'],
    'distance': [456,123],
    'lat': [13123,12434],
    'long': [123124,46788]}

ls = pd.DataFrame(testData)

print(ls)

print(heapSortByDistance(ls, 2))