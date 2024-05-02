from node import DoubleNode

class DoublyList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.size = 0
    
    def __find_node(self, pos):
        tmpNode = self.__head
        for i in range(1, pos):
            tmpNode = tmpNode.next
        return tmpNode
    
    def __insert_node_at_begin(self, data):
        newNode = DoubleNode(data)
        if(self.__head == None):
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__head.prev = newNode
            newNode.next = self.__head
            self.__head = newNode
    
    def __insert_node_at_end(self, data):
        newNode = DoubleNode(data)
        if(self.__tail == None):
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
    
    def __insert_node_at_pos(self, pos, data):
        tmpNode = self.__find_node(pos)
        newNode = DoubleNode(data)
        newNode.next = tmpNode.next
        tmpNode.next.prev = newNode
        tmpNode.next = newNode
        newNode.prev = tmpNode

    def __delete_node_at_begin(self):
        delete_node = self.__head
        self.__head = self.__head.next
        del delete_node
    
    def __delete_node_at_end(self):
        delete_node = self.__tail
        self.__tail.prev.next = self.__tail.next
        self.__tail = self.__tail.prev
        del delete_node

    def __delete_node_at_pos(self, pos):
        tmpNode = self.__find_node(pos)
        delete_node = tmpNode.next
        tmpNode.next = tmpNode.next.next
        tmpNode.next.next.prev = tmpNode
        del delete_node
    
    # accessable function 
    def get_head_node(self):
        return self.__head
    
    def get_tail_node(self):
        return self.__tail
        
    def insert_node(self, pos, data):
        if(pos >= 0 and pos <= self.size):
            if(pos == 0):
                self.__insert_node_at_begin(data)
            elif(pos == self.size):
                self.__insert_node_at_end(data)
            else:
                self.__insert_node_at_pos(pos, data)
            self.size += 1
        else:
            print('Invalid position')
    
    def delete_node(self, pos):
        if(pos >= 0 and pos < self.size):
            if(pos == 0):
                self.__delete_node_at_begin()
            elif(pos == self.size-1):
                self.__delete_node_at_end()
            else:
                self.__delete_node_at_pos(pos)
            self.size -= 1
        else:
            print('Invalid position')


    def print_by_pos(self, pos):
        tmpNode = self.__head
        for i in range(0, pos):
            tmpNode = tmpNode.next
        print(tmpNode.data)
    
    def print_list(self):
        tmpNode = self.__head
        while(tmpNode != None):
            print(tmpNode.data, end=' ')
            tmpNode = tmpNode.next
        print()
