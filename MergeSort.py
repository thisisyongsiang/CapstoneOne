import json

class MergeSort:
    """
    Class For MergeSort
    Sorts at initialization
    call GetNextN to get the next n values after sorting
    call GetPrevN to get prev n values after sorting
    """
    def __init__(self,arrayToSort,field,isAscending=True):
        self.list=arrayToSort
        self.field=field
        self.index=0
        self.isAscending=isAscending
        self.sort(0,len(self.list)-1,lambda a,b:a[field]<=b[field])

    def ChangeField(self,field):
        """
        Sorts the data again based on the new field
        """
        self.field=field
        if self.isAscending:
            self.sort(0,len(self.list)-1,lambda a,b:a[field]<=b[field])
        self.index=0
    def ChangeOrder(self,isAscending:bool):
        '''
        Change the sorting order of the data
        '''
        if self.isAscending != isAscending:
            self.isAscending=isAscending
            self.index=0
    def GetNextN(self,n):
        if self.index==len(self.list)-1:
            return []
        index=self.index
        self.index+=n
        if self.index>=len(self.list):
            self.index=len(self.list)-1
        if self.isAscending:
            return self.list[index:self.index]
        else:
            output=self.list[len(self.list)-index-n:len(self.list)-index]
            output.reverse()
            return output
    def GetPrevN(self,n):
        self.index-=n
        if self.index<=0:
            return None
        index=self.index
        self.index-=n
        if self.index<0:
            self.index=0
        if self.isAscending:
            return self.list[self.index:index]
        else:
            output=self.list[len(self.list)-self.index-n:len(self.list)-self.index]
            output.reverse()
            return output

    def merge(self,l,m,r,comparer):
        res=[]
        lp=l
        rp=m+1
        while lp<=m and rp<=r:
            if comparer( self.list[lp], self.list[rp]):
                res.append( self.list[lp])
                lp+=1
            else:
                res.append( self.list[rp])
                rp+=1
        while lp<=m:
            res.append( self.list[lp])
            lp+=1
        while rp<=r:
            res.append( self.list[rp])
            rp+=1
        for i in range(len(res)):
             self.list[i+l]=res[i]

    def sort(self ,l,r,comparer):
        if l<r:
            m=(l+r)//2
            self.sort(l,m,comparer)
            self.sort(m+1,r,comparer)
            self.merge(l,m,r,comparer)



# def merge(arr,l,m,r,comparer):
#     res=[]
#     lp=l
#     rp=m+1
#     while lp<=m and rp<=r:
#         if comparer(arr[lp],arr[rp]):
#             res.append(arr[lp])
#             lp+=1
#         else:
#             res.append(arr[rp])
#             rp+=1
#     while lp<=m:
#         res.append(arr[lp])
#         lp+=1
#     while rp<=r:
#         res.append(arr[rp])
#         rp+=1
#     for i in range(len(res)):
#         arr[i+l]=res[i]

# def mergeSort(arr,l,r,comparer):
#     if l<r:
#         m=(l+r)//2
#         mergeSort(arr,l,m,comparer)
#         mergeSort(arr,m+1,r,comparer)
#         merge(arr,l,m,r,comparer)

# def getFirstN(arr,field,k,IsAscending=True):
#     '''
#     Returns first N Items in sorted array based on field
#     using mergeSort
#     '''
#     if IsAscending:
#         mergeSort(arr,0,len(arr)-1,lambda a,b:a[field]<=b[field])
#     else:
#         mergeSort(arr,0,len(arr)-1,lambda a,b:a[field]>b[field])
#     if len(arr)<=k:
#         return (arr)
#     return arr[0:k]

def example():
    dir="singaporeFnBAll.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)
    mergSort=MergeSort(data,'review_count',False)

    firstN=mergSort.GetNextN(5)
    [print(c['name'],c['review_count']) for c in firstN]
    print('done')
    firstN=mergSort.GetNextN(5)
    [print(c['name'],c['review_count']) for c in firstN]
    print('done')
    firstN=mergSort.GetPrevN(5)
    [print(c['name'],c['review_count']) for c in firstN]
    print('done')

example()