from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def pop(self):
        tmpNode = self.head
        self.head = self.head.next
        del tmpNode
        self.size -= 1
    
    def top(self):
        return self.head.data

    def is_empty(self):
        if(self.size == 0):
            return True
        else:
            return False

    def size(self):
        return self.size