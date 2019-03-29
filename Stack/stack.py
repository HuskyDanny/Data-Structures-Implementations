class Stack:

    def __init__(self,input = None):
        self.capacity = 100
        self.array = [None] * self.capacity
        self.last = 0
        if input:
            for val in input:
                self.array[self.last] = val
                self.last += 1

    def pop(self):
        value = self.array[self.last]
        self.array[self.last] = None
        self.last -= 1
        return value

    def push(self,val):
        if self.last == self.capacity - 1:
            resize()
        self.last += 1
        self.array[self.last] = val

    def isEmpty():
        return self.last == 0

    
