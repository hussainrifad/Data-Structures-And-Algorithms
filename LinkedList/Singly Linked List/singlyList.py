from node import SingleNode

class SinglyList:
    def __init__(self):
        self.__head = None
        self.__tmp = None
        self.__size = 0
    
    def __get_node_at_pos(self, pos):
        tmpNode = self.__head
        for i in range(1, pos):
            tmpNode = tmpNode.next
        return tmpNode
    
    def __insert_begin(self, data):
        newNode = SingleNode(data)
        if(self.__head == None):
            self.__head = newNode
            self.__tmp = self.__head
        else:
            newNode.next = self.__head
            self.__head = newNode
        self.__size += 1

    def __insert_end(self, data):
        newNode = SingleNode(data)
        if(self.__head == None):
            self.__head = newNode
            self.__tmp = self.__head
        else:
            self.__tmp.next = newNode
            self.__tmp = newNode

    def __insert_at_pos(self, pos, data):
        newNode = SingleNode(data)
        tmpNode = self.__get_node_at_pos(pos)
        newNode.next = tmpNode.next
        tmpNode.next = newNode
    
    def __delete_node_begin(self):
        deleteNode = self.__head
        self.__head = self.__head.next

    def __delete_node_pos(self, pos):
        tmpNode = self.__get_node_at_pos(pos)
        deleteNode = tmpNode.next
        tmpNode.next =tmpNode.next.next

    # accessable function 
    def get_head_node(self):
        return self.__head
    
    def insert_node(self, pos, data):
        if(pos <= self.__size and pos >= 0):
            if(pos == self.__size):
                self.__insert_end(data)
            elif(pos == 0):
                self.__insert_begin(data)
            else:
                self.__insert_at_pos(pos, data)
            self.__size += 1
        else:
            print('Invalid position')

    def delete_node(self, pos):
        if(pos >= 0 and pos < self.__size):
            if(pos == 0):
                self.__delete_node_begin()
            else:
                self.__delete_node_pos(pos)
            self.__size -= 1
        else:
            print('Invalid position')
    
    def printList(self):
        tmpNode = self.__head
        while(tmpNode != None):
            print(tmpNode.data, end=' ')
            tmpNode = tmpNode.next
        print()
    
    def print_data_in_pos(self, pos):
        if(pos >= 0 and pos < self.__size):
            node = self.__head
            for i in range(0, pos):
                node = node.next
            print(node.data)
        else:
            print('Invalid position')

# in object we can only use functions 
# 1. insert_node
# 2. delete_node
# 3. printList
# 4. print_data_in_pos
