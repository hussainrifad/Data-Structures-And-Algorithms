from node import TreeNode

class BinaryTee:
    def __init__(self):
        self.root = None
    
    def insert_data(self):
        queue = []
        rt = int(input())
        if(rt != -1): self.root = TreeNode(rt)
        
        if(self.root):
            queue.append(self.root)
        
        while(len(queue) != 0):
            parentNode = queue[0]
            queue.pop(0)

            left = int(input())
            right = int(input())

            leftNode = None
            rightNode = None

            if(left != -1):
                leftNode = TreeNode(left)
                queue.append(leftNode)
            if(right != -1):
                rightNode = TreeNode(right)
                queue.append(rightNode)

            parentNode.left = leftNode
            parentNode.right = rightNode
        
    def get_rootNode(self):
        return self.root
    
    def print_tree_preOrder(self, node):
        if(node == None):
            return
        print(node.data)
        self.print_tree_preOrder(node.left)
        self.print_tree_preOrder(node.right)

    def print_tree_postOrder(self, node):
        if(node == None):
            return
        self.print_tree_postOrder(node.left)
        self.print_tree_postOrder(node.right)
        print(node.data)

    def print_tree_inOrder(self, node):
        if(node == None):
            return
        self.print_tree_inOrder(node.left)
        print(node.data)
        self.print_tree_inOrder(node.right)
    
    def print_tree_levelOrder(self, node):
        queue = []
        pair = (0, node)
        if(node):
            queue.append(pair) 

        while(len(queue) != 0):
            parent = queue[0][1]
            level = queue[0][0]
            queue.pop(0)
            print(f'Level -> {level} valie : {parent.data}')

            if(parent.left):
                queue.append((level+1, parent.left))
            
            if(parent.right):
                queue.append((level+1, parent.right))
        