from node import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def convert(self, arr, node, l, r):
        if (l > r):
            return None
        
        mid = (l+r)//2
        node = BSTNode(arr[mid])
        if(self.root == None):
            self.root = node
        node.left = self.convert(arr, node.left, l, mid-1)
        node.right = self.convert(arr, node.right, mid+1, r)
        return node
    
    def printTree(self, node):
        if(node == None):
            return
        
        self.printTree(node.left)
        print(node.data, end= ' ')
        self.printTree(node.right)

arr = [1, 2, 4, 5, 6, 7, 8, 10, 20, 50, 60]
tree = BinarySearchTree()
tree.convert(arr, tree.root, 0, len(arr)-1)
print(tree.root)
tree.printTree(tree.root)