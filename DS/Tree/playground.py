from binary_search_tree import *

# Usage of BinarySearchTree

bstree = BinarySearchTree()
bstree.insert(23)
bstree.insert(11)
bstree.insert(31)

print('root', bstree.root.value)
print('left', bstree.root.left.value)
print('right', bstree.root.right.value)

print(bstree.contains(23))

# Breadth first search

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.bfs())
print(my_tree.dfs_preorder())
print(my_tree.dfs_postorder())
print(my_tree.dfs_in_order())
