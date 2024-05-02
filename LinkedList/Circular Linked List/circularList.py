from node import CircularNode

class CircularList:
    def __init__(self):
        self.head = None
        self.tmp = None
    
    def insert_node(self, data):
        newNode = CircularNode(data)
        if(self.head == None):
            self.head = newNode
            self.tmp = newNode