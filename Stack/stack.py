from node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            self.tail = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
    
    def pop(self):
        if(self.size == 1):
            del self.tail
        else:
            tmpNode = self.tail
            self.tail.prev.next = self.tail.next
            self.tail = tmpNode.prev
            del tmpNode
        self.size -= 1
    
    def is_empty(self):
        if(self.size == 0):
            return True
        else:
            return False
    
    def size(self):
        return self.size

    def top(self):
        return self.tail.data
    
    def get_tail(self):
        return self.tail
