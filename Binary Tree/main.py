from binary_tree import BinaryTee
# main 
myTree = BinaryTee()
myTree.insert_data()
myTree.print_tree_preOrder(myTree.get_rootNode())
myTree.print_tree_levelOrder(myTree.get_rootNode())