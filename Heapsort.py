class Heap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
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
        
    def Heapit(self, pos, comparer):

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
    
    def generateHeap(self, comparer):

        for pos in range(self.size//2, 0, -1):
            self.Heapit(pos, comparer)
    
    def remove(self, comparer):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT]= self.Heap[self.size-1]
        self.size -= 1
        self.Heapit(self.FRONT, comparer)
        return popped

    def Print(self):
        for i in range(1, self.maxsize//2+1, 1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))


def getFirstN(arr, field, topN, isAscending=True):

    """
    Takes in list of dictionaries, field for sorting and boolean value for ascending/descending order of sort and returns top N items in a list of dictionaries
    """

    topN = min(topN, len(arr))
    sortedList = []

    if isAscending == True:
        newHeap = Heap(len(arr))
        for i in range(len(arr)):
            newHeap.insert(arr[i],lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance']))
        for j in range(topN):
            sortedList.append(newHeap.remove(lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance'])))
        
    else:
        newHeap = Heap(len(arr))
        for i in range(len(arr)):
            newHeap.insert(arr[i], lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance']))
        for j in range(topN):
            sortedList.append(newHeap.remove(lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance'])))
        
    return sortedList