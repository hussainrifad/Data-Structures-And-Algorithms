from node import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def __insert_data(self, node, data):
        if(data < node.data):
            if(node.left == None):
                node.left = BSTNode(data)
            else:
                self.__insert_data(node.left, data)
        elif(data > node.data):
            if(node.right == None):
                node.right = BSTNode(data)
            else:
                self.__insert_data(node.right, data)

    def insert(self, data):
        if(self.__root == None):
            self.__root = BSTNode(data)
        else:
            self.__insert_data(self.__root, data)

    def printTree(self, root):
        if(root == None):
            return
        
        print(root.data, end=' ')
        self.printTree(root.left)
        self.printTree(root.right)

    def search(self, root, data):
        if(root.data == data):
            return True
        if(root == None):
            return False

        if(data < root.data):
            return self.search(root.left, data)
        elif(data > root.data):
            return self.search(root.right, data)
        

tree = BinarySearchTree()
tree.insert(100)
tree.insert(30)
tree.insert(200)
tree.insert(150)
tree.insert(500)
tree.insert(300)
tree.insert(225)
tree.insert(175)
tree.insert(60)
tree.printTree(tree.get_root())
print(tree.search(tree.get_root(), 300))
