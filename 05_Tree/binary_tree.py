class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def size(self):
        if self.left:
            l = self.left.size()
        else:
            l = 0

        if self.right:
            r = self.right.size()
        else:
            r = 0

        return l + r + 1
    
    def depth(self):
        if self.left:
            l = self.left.depth()
        else:
            l = 0
        
        if self.right:
            r = self.right.depth()
        else:
            r = 0

        return max(l, r) + 1
    
    def in_order(self):
        if self.left != None:
            self.left.in_order()

        print(self.data)

        if self.right != None:
            self.right.in_order()

    def pre_order(self):
        print(self.data)

        if self.left != None:
            self.left.pre_order()
        
        if self.right != None:
            self.right.pre_order()

    def post_order(self):
        if self.left != None:
            self.left.post_order()
        
        if self.right != None:
            self.right.post_order()

        print(self.data)


class BinaryTree():
    def __init__(self, root):
        self.root = root

    def size(self):
        return self.root.size()
    
    def depth(self):
        return self.root.depth()
    
    def in_order(self):
        print('in-order traversal start')
        return self.root.in_order()
    
    def pre_order(self):
        print('pre-order traversal start')
        return self.root.pre_order()
    
    def post_order(self):
        print('post-order traversal start')
        return self.root.post_order()

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
