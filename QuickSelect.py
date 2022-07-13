import json
from random import random, randrange

class QuickSelect:
    def __init__(self,data,field,isAscending=True) -> None:
        self.data=data
        self.field=field
        self.isAscending=isAscending
        self.index=0
    def ChangeField(self,field):
        self.field=field
        self.index=0
    def ChangeOrder(self,isAscending:bool):
        if self.isAscending!=isAscending:
            self.isAscending=isAscending
            self.index=0
    def GetNextN(self,n):
        arr=[]
        if self.index==len(self.data):
            return arr
        if self.isAscending:
            self.quickSelect(self.index,len(self.data)-1,n+self.index,lambda a,b:a[self.field]<=b[self.field])
        else:
            self.quickSelect(self.index,len(self.data)-1,n+self.index,lambda a,b:a[self.field]>b[self.field])
        if self.index+n>=len(self.data):
            arr=self.data[self.index:]
            self.index=len(self.data)-1
        else:
            arr=self.data[self.index:self.index+n]
            self.index+=n
        return arr
    def GetPrevN(self,n):
        self.index-=n
        if self.index<=0:
            return []
        index=self.index
        self.index-=n
        return self.data[self.index:index]
    
    def swapElements(self,arr,i,j):
        """
        swap item of index i and 
        item of index j of array arr
        """
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp

    def partition(self,l,r,comparer):
        """
        Partition will use random pivot
        """
        self.swapElements(self.data,l,randrange(l,r+1))
        pivot=self.data[l]
        m=l
        for i in range(l+1,r+1):
            if comparer(self.data[i],pivot):
                m=m+1
                self.swapElements(self.data,m,i)
        self.swapElements(self.data,m,l)
        return m
                

    def quickSelect(self,l,r,k,comparer):
        if l==r:
            return self.data[k]
        pivIdx=self.partition(l,r,comparer)
        
        if pivIdx==k-1:
            return self.data[:pivIdx+1]
        elif pivIdx>=k:
            return self.quickSelect(l,pivIdx-1,k,comparer)
        else:
            return self.quickSelect(pivIdx+1,r,k,comparer)

# def getFirstN(arr,field,k,IsAscending=True):
#     '''
#     Returns first N Items in based on field
#     using quickselect
#     '''
#     if len(arr)<=k:return arr
#     if IsAscending:
#         return quickSelect(arr,0,len(arr)-1,k,lambda a,b:a[field]<=b[field])
#     else:
#         return quickSelect(arr,0,len(arr)-1,k,lambda a,b:a[field]>b[field])


def example():
    dir="yelpAPIData.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)
    qs=QuickSelect(data,'review_count',False)
    # firstN=getFirstN(data,'review_count',10,False)
    firstN=qs.GetNextN(5)
    [print(c['name'],c['review_count']) for c in firstN]
    print('done')
    firstN=qs.GetNextN(5)
    [print(c['name'],c['review_count']) for c in firstN]
    print('done')   
    firstN=qs.GetPrevN(5)
    [print(c['name'],c['review_count']) for c in firstN]
    print('done')
