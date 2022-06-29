import json
from random import random, randrange

def swapElements(arr,i,j):
    """
    swap item of index i and 
    item of index j of array arr
    """
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def partition(arr,l,r,comparer):
    swapElements(arr,l,randrange(l,r+1))
    pivot=arr[l]
    m=l
    for i in range(l+1,r+1):
        if comparer(arr[i],pivot):
            m=m+1
            swapElements(arr,m,i)
    swapElements(arr,m,l)
    return m
            

def quickSelect(arr,l,r,k,comparer):
    if l==r:
        return arr[:k]
    pivIdx=partition(arr,l,r,comparer)
    
    if pivIdx==k-1:
        return arr[:pivIdx+1]
    elif pivIdx>=k:
        return quickSelect(arr,l,pivIdx-1,k,comparer)
    else:
        return quickSelect(arr,pivIdx+1,r,k,comparer)

def getFirstN(arr,field,k,IsAscending=True):
    '''
    Returns first N Items in based on field
    using quickselect
    '''
    if IsAscending:
        return quickSelect(arr,0,len(arr)-1,k,lambda a,b:a[field]<=b[field])
    else:
        return quickSelect(arr,0,len(arr)-1,k,lambda a,b:a[field]>b[field])


def example():
    dir="yelpAPIData.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)
    firstN=getFirstN(data,'review_count',10,False)
    [print(c['name'],c['review_count']) for c in firstN]