import json

def merge(arr,l,m,r,comparer):
    res=[]
    lp=l
    rp=m+1
    while lp<=m and rp<=r:
        if comparer(arr[lp],arr[rp]):
            res.append(arr[lp])
            lp+=1
        else:
            res.append(arr[rp])
            rp+=1
    while lp<=m:
        res.append(arr[lp])
        lp+=1
    while rp<=r:
        res.append(arr[rp])
        rp+=1
    for i in range(len(res)):
        arr[i+l]=res[i]

def mergeSort(arr,l,r,comparer):
    if l<r:
        m=(l+r)//2
        mergeSort(arr,l,m,comparer)
        mergeSort(arr,m+1,r,comparer)
        merge(arr,l,m,r,comparer)

def getFirstN(arr,field,k,IsAscending=True):
    '''
    Returns first N Items in sorted array based on field
    using mergeSort
    '''
    if IsAscending:
        mergeSort(arr,0,len(arr)-1,lambda a,b:a[field]<=b[field])
    else:
        mergeSort(arr,0,len(arr)-1,lambda a,b:a[field]>b[field])
    return arr[0:k]

def example():
    dir="yelpAPIData.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)
    firstN=getFirstN(data,'review_count',10,False)
    [print(c['name'],c['review_count']) for c in firstN]
example()