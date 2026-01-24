from binary_tree import Node, BinaryTree

x1 = Node(5)
x2 = Node(17)
x3 = Node(23)
x4 = Node(44)
x5 = Node(36)
x6 = Node(67)

tree = BinaryTree(x1)
x1.left = x2
x2.left = x3
x2.right = x4
x1.right = x5
x5.right = x6

# structure
#             5
#         /      \
#       17        36
#    /      \         \
#  23       44         67
#

print(f'tree size: {tree.size()}')
print(f'tree depth: {tree.depth()}')
tree.in_order()
tree.pre_order()
tree.post_order()
