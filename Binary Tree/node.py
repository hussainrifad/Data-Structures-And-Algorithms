# ---------- Basic Operations On Binary Tree ----------
# 1. Inserting an element.
# 2. Removing an element.
# 3. Searching for an element.
# 4. Deletion for an element.
# 5. Traversing an element. There are four (mainly three) types of traversals in a binary tree which will be discussed ahead.

# ---------- Auxiliary Operations On Binary Tree ---------
# 1. Finding the height of the tree
# 2. Find the level of the tree
# 3. Finding the size of the entire tree.

# ------------ Properties of Binary Tree ------------
# 1. The maximum number of nodes at level ‘l’ of a binary tree is 2^l 
# 2. The Maximum number of nodes in a binary tree of height ‘h’ is 2^h – 1 
# 3. In a Binary Tree with N nodes, the minimum possible height or the minimum number of levels is Log2(N+1)
# 4. A Binary Tree with L leaves has at least | Log2L |+ 1   levels 
# 5. In a Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children
# 5. In a Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children
# 6. In a non-empty binary tree, if n is the total number of nodes and e is the total number of edges, then e = n-1 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
