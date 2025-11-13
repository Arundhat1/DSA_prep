class Solution:
    def right(i):
        if len(self.heap) -1 < 2*i+1 :
            return None
        else:
            return self.heap[2*i+1]
    def left(i):
        if len(self.heap) -1 < 2*i+2 :
            return None
        else:
            return self.heap[2*i+2]
    def parent(i):
        if 0  < i :
            return None
        else:
            return self.heap[(i-1)//2]
    def bubbleup(i):
        while parent(i) and parent(i) > self.heap[i]:
            parent(i),self.heap[i] = self.heap[i],parent[i]
            i = (i-1)//2
    def bubbledown(i):
        size = len(self.heap)
        
    def initializeHeap(self):
        self.heap = []
        return self.heap

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) -1
        
        while self.heap[(i-1)//2] and self.heap[(i-1)//2] > key:
            self.heap[(i-1)//2],self.heap[-1] = self.heap[-1],self.heap[(i-1)//2]
            i = (i-1) //2
        

    def changeKey(self, index, new_val):
         old_val = self.heap(index)
         self.heap[index] = new_val

         if old_val < new_val:
            self.bubbledown(index)
        else:
            self.bubbleup(index)
            

    def extractMin(self):
        mini = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        delf.bubbledown(0)
        return mini
        


    def isEmpty(self):
        return len(self.heap) == 0

    def getMin(self):
        return self.heap[0]

    def heapSize(self):
        return len(self.heap)
