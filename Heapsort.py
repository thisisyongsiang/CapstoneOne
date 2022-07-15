from locale import currency
import sys
import json

class Heap:

    def __init__(self, arr):
        self.maxsize = sys.maxsize
        self.size = len(arr)
        self.Heap = arr
        self.FRONT = 0

    
    def parent(self, pos):
        return (pos-1)//2 if pos != 0 else 0
    
    def leftChild(self, pos):
        return (2*pos)+1

    def rightChild(self, pos):
        return (2*pos)+2
    
    def isLeaf(self, pos):
        return (2*pos)+1 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    
    def bubbleDown(self, pos, comparer):

        child = self.leftChild(pos)
        done = False

        while child < self.size and not done:
            rightC = self.rightChild(pos)
            if rightC < self.size and comparer(self.Heap[child], self.Heap[rightC]):
                child = rightC

            if comparer(self.Heap[pos], self.Heap[child]):
                self.swap(pos, child)
            else:
                done = True
            
            pos = child
            child = self.leftChild(pos)

    
    def insert(self, item, comparer):
        if self.size >= self.maxsize:
            return
        self.Heap[self.size] = item
        curr = self.size

        self.size += 1

        while comparer(self.Heap[self.parent(curr)],self.Heap[curr]):
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
    
    def heapify(self, comparer):

        for pos in range(self.parent(self.size-1), -1, -1):
            self.bubbleDown(pos, comparer)
    
    def remove(self, comparer):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT]= self.Heap[self.size-1]
        self.size -= 1
        self.bubbleDown(self.FRONT, comparer)
        return popped

    def Print(self):
        for i in range(0, self.parent(self.size-1), 1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))

class getItemsByField:

    """
    Class to heapify array and retrieve top items. Takes in list of dictionaries, field for sorting and boolean value for ascending/descending order of sort.
    """

    def __init__(self, arr, field, isAscending=True):
        self.arr = arr
        self.field = field
        self.isAscending = isAscending
        self.newHeap = Heap(arr)
        self.removedCount = 0
        self.removedItems = []
        self.currIndex = 0
        self.lastExtractedN = 0

    def getNextN(self, nextN):
        """
        Returns top N items in a list of dictionaries
        """

        def ascendingComparer(a,b):
             return a[self.field]+(1/a['distance'])>b[self.field]+(1/b['distance'])

        def descendingComparer(a,b):
            return a[self.field]+(1/a['distance'])<b[self.field]+(1/b['distance'])

        if self.currIndex + nextN > len(self.arr):
            nextN = len(self.arr)-self.currIndex

        sortedList = []

        #only heapify during first call to getNextN
        if self.removedCount == 0:
            self.newHeap.heapify(ascendingComparer if self.isAscending == True else descendingComparer)
        

        if nextN + self.currIndex <= self.removedCount: #case when calling nextN after calling prevN when all items in question have already been removed from heap
            self.currIndex += nextN
            return self.removedItems[self.currIndex-nextN : self.currIndex]
        elif nextN + self.currIndex > self.removedCount and self.currIndex == self.removedCount: #case for when calling nextN when all N items have not previously been removed from heap
            for j in range(nextN):
                sortedList.append(self.newHeap.remove(ascendingComparer if self.isAscending == True else descendingComparer))
                self.currIndex += 1
                self.removedCount += 1
        elif nextN + self.currIndex >= self.removedCount and self.currIndex < self.removedCount: #case for when some of nextN items have been removed from heap previously and remaining of subset of N items need to be removed from heap
            sortedList += self.removedItems[self.currIndex : self.removedCount]
            self.currIndex = self.removedCount
            for j in range(nextN-(self.removedCount-self.currIndex)):
                sortedList.append(self.newHeap.remove(ascendingComparer if self.isAscending == True else descendingComparer))
                self.currIndex += 1
                self.removedCount += 1

        self.lastExtractedN = nextN
        self.removedItems += sortedList

        return sortedList

    def getPrevN(self, prevN):
        """
        Function returns previous N elements that have been extracted from the heap in sorted order.
        Function is designed to work with non-consistent values of N.
        """

        if self.currIndex - self.lastExtractedN <= 0: #return nothing if trying to get prevN before extracting 2 times
            return
        elif self.currIndex - self.lastExtractedN - prevN <= 0: #case for when extracting all remaining items from sorted array
            self.currIndex = self.currIndex - self.lastExtractedN
            self.lastExtractedN = self.currIndex - self.lastExtractedN
            return self.removedItems[0 : self.currIndex]
        else:
            self.currIndex = self.currIndex-self.lastExtractedN #case for when extracting subset of remaining items from sorted array
            self.lastExtractedN = prevN
            return self.removedItems[self.currIndex-prevN : self.currIndex]
        
    
def example():
    dir="yelpAPIData.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)

    temp = getItemsByField(data, 'distance', True)

    for i in range(5):
        output = temp.getNextN(5)

        print(i)
        for j in range(len(output)):
            print(output[j]['name'], output[j]['distance'])

    output2 = temp.getPrevN(3)
    for k in range(len(output2)):
            print(output2[k]['name'], output2[k]['distance'])

    output2 = temp.getPrevN(3)
    for k in range(len(output2)):
            print(output2[k]['name'], output2[k]['distance'])

    output2 = temp.getNextN(3)
    for k in range(len(output2)):
            print(output2[k]['name'], output2[k]['distance'])

