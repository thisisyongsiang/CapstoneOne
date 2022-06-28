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

    sortedList = []

    for i in range(topX):
        sortedList.append(heapq.heappop(heap_dict))
    
    sortedDf = pd.DataFrame(sortedList, columns=['distance','id'])
    outputDf = pd.merge(sortedDf, bizData, on='id', how='left')
    outputDf = outputDf.drop(['distance_y'], axis=1)
    outputDf.rename(columns={'distance_x':'distance'}, inplace=True)
    
    return outputDf

def heapSortByReview(bizData, topX):
    ''' takes in Pandas dataframe with rating and id field and sorts via heapsort
    returns a sorted dataframe'''

    heap_dict = []

    #create list of tuples for sorting via heapsort and heapify it
    #adds postal code as decimals to make each value unique
    #sorts for maximum rating using existing heapify algorithm by applying negative multiplier on rating values

    for i in range(len(bizData.index)):
        heap_dict.append((-1*(bizData['rating'][i]),bizData['id'][i]))

    heapq.heapify(heap_dict)

    sortedList = []

    for i in range(topX):
        sortedList.append(heapq.heappop(heap_dict))
    
    sortedDf = pd.DataFrame(sortedList, columns=['rating','id'])
    outputDf = pd.merge(sortedDf, bizData, on='id', how='left')
    outputDf = outputDf.drop(['rating_y'], axis=1)
    outputDf.rename(columns={'rating_x':'rating'}, inplace=True)
    outputDf['rating'] = outputDf['rating'].apply(lambda x: x*-1)
    
    return outputDf

def heapSortByPrice(bizData, topX, sortOrder):
    ''' takes in Pandas dataframe with price and id field and sorts via heapsort
    returns a sorted dataframe'''
    #requires sortOrder as argument, where sortOrder can be 'ascending' or 'descending' order of price for sorting

    heap_dict = []

    if sortOrder.lower() == 'ascending' or sortOrder.lower() == "descending":
        if sortOrder.lower() == 'ascending':
            for i in range(len(bizData.index)):
                heap_dict.append((len(bizData['price'][i]),bizData['id'][i]))
        else:
            for i in range(len(bizData.index)):
                heap_dict.append((-1*len(bizData['price'][i]),bizData['id'][i]))
    else:
        print('invalid sort order')
        return

    heapq.heapify(heap_dict)

    sortedList = []

    for i in range(topX):
        sortedList.append(heapq.heappop(heap_dict))
    
    sortedDf = pd.DataFrame(sortedList, columns=['price','id'])
    
    outputDf = pd.merge(sortedDf, bizData, on='id', how='left')
    outputDf = outputDf.drop(['price_y'], axis=1)
    outputDf.rename(columns={'price_x':'price'}, inplace=True)
    outputDf['price'] = outputDf['price'].apply(lambda x: x*'$' if sortOrder == 'ascending' else (x*-1)*'$')
    
    return outputDf

testData = {
    'id': ['test1','t2]'],
    'distance': [456,123],
    'lat': [13123,12434],
    'long': [123124,46788],
    'rating': [4.6, 4.9],
    'price': ['$', '$$']}

ls = pd.DataFrame(testData)

print(heapSortByDistance(ls, 2))
print(heapSortByPrice(ls, 2, 'descending'))
print(heapSortByReview(ls, 2))