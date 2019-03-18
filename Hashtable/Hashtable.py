class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value

class Hashtable:
            
    def __init__(self):
        self.array = [0] * 100
        self.size = len(self.array)
        
    def hashvalue(self, key):
        return sum([ ord(i) for i in key]) % self.size

    def add(self, node):
        index = self.hashvalue(node.getKey())
        temp = Node(node.getKey(), node.getValue())
        if not self.array[index]:
            self.array[index] = temp
        else:
            curr = self.array[index]
            while curr.next:
                curr = curr.next
            curr.next = temp
        
    def get(self, key):
        index = self.hashvalue(key)
        curr = self.array[index]
        while curr:
            if curr.key == key:
                return Node(curr.key, curr.value)
        return None
