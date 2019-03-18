class minHeap:
    def __init__(self):
        self.heap = []

    def findParent(self, index):
        return (index-1)//2

    def findChild(self,index):
        return index * 2 + 1, index * 2 + 2

    def percolateUp(self, index):
        parent = self.findParent(index)
        if self.heap[parent] <= self.heap[index] or parent < 0: return
        if self.heap[parent] > self.heap[index]:
            self.swap(parent, index)
        self.percolateUp(parent)

    def swap(self, indexi, indexj):
        temp = self.heap[indexi]
        self.heap[indexi] = self.heap[indexj]
        self.heap[indexj] = temp
    
    def add(self, value):
        self.heap.append(value)
        self.percolateUp(len(self.heap)-1)

    
    def deleteMin(self):
        if not self.heap : raise Exception('The heap is empty')
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.percolateDown(0)
        return result
        
    def percolateDown(self, index):
        left,right = self.findChild(index)
        next_index = -1
        if left >= len(self.heap) or right >= len(self.heap): return
        
        if self.heap[left] > self.heap[right]:
            next_index = right
        else:
            next_index = left
        if next_index != -1:
            self.swap(index, next_index)
        self.percolateDown(next_index)
            
            
    