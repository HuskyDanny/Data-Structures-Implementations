#Adjacent Lists
#Pass in with any objects
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.nameToInt = { self.vertices[i] : i for i in range(len(self.vertices))}
        self.bucket = [None] * len(self.vertices)

    def addEdge(self,start,end):
        start = self.nameToInt[start]
        end = self.nameToInt[end]

        node = self.Node(end)
        node.next = self.bucket[start]
        self.bucket[start] = node


    def toString(self):
        for i in range(len(self.vertices)):
            print("The current vertex is {}\n".format(self.vertices[i]))
            curr = self.bucket[i]
            print(self.vertices[i], end='')
            while curr :
                print("->{}".format(self.vertices[curr.val]))
                curr = curr.next
            print("\n")

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
#Example:
'''
y = Person('Yaya', 15)
l = Person('Junchen', 18)
graph = Graph([y,l])
graph.addEdge(y,l)
graph.toString()
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name
