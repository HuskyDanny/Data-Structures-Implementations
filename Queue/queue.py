#Basic Queue
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None

    def enqueue(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        else:
            self.tail = node

    def dequeue(self):
        if not self.head:
            raise Exception("The Queue is empty")
        value = self.head.value
        self.head = self.head.next
        print("deleted {}".format(value))

    def peek(self):
        print(self.head.value)
