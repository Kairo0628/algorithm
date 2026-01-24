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


class BinaryTree():
    def __init__(self, root):
        self.root = root

    def size(self):
        return self.root.size()
    
    def depth(self):
        return self.root.depth()


x1 = Node(5)
x2 = Node(17)
x3 = Node(23)
x4 = Node(44)

tree = BinaryTree(x1)
x1.left = x2
x2.left = x3
x2.right = x4

print(tree.size())

print(tree.depth())

#
#           x1
#         /
#        x2 
#      /    \
#     x3    x4
#