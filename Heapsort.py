import sys

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
        self.removeCount = 0

    def getTopN(self, topN):
        """
        Returns top N items in a list of dictionaries
        """

        topN = min(topN, len(self.arr)-self.removeCount)
        sortedList = []
        
        if self.isAscending == True:
            self.newHeap.heapify(lambda a,b: a[self.field]+(1/a['distance'])>b[self.field]+(1/b['distance']))
            for j in range(topN):
                sortedList.append(self.newHeap.remove(lambda a,b: a[self.field]+(1/a['distance'])>b[self.field]+(1/b['distance'])))
        else:
            self.newHeap.heapify(lambda a,b: a[self.field]+(1/a['distance'])<b[self.field]+(1/b['distance']))
            for j in range(topN):
                sortedList.append(self.newHeap.remove(lambda a,b: a[self.field]+(1/a['distance'])<b[self.field]+(1/b['distance'])))

        self.removeCount += topN

        return sortedList



#sample code for using class and retrieving multiple topN items 
# temp = getItemsByField(yelp_data, 'distance', True)

# for i in range(2):
#     output = temp.getTopN(5)

#     # print(output)
#     for j in range(len(output)):
#         print(output[j]['name'], output[j]['distance'])