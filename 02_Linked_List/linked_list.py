class Node:
    def __init__(self, n):
        self.data = n
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail

    def display(self):
        result = []
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
            result.append(curr.data)

        print(result)

    def get(self, index):
        if index > self.size - 1 or index < -1:
            raise IndexError()
    
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        
        return curr
    
    def insert(self, node: Node, index = None):
        if index == None:
            index = self.size
            
        if index > self.size + 1:
            raise IndexError()
        elif index < 0:
            raise IndexError()
        
        prev = self.get(index - 1)
        curr = prev.next

        prev.next = node
        node.next = curr

        self.size += 1

    def delete(self, index = None):
        if index == None:
            index = self.size - 1

        if index > self.size or index < 0:
            raise IndexError()

        prev = self.get(index - 1)
        curr = prev.next

        prev.next = curr.next

        self.size -= 1

        return curr

    def concat(self, other: 'LinkedList'):
        if other.size == 0:
            return

        last = self.get(self.size - 1)
        first = other.head.next
        last.next = first

        new_last = other.get(other.size - 1)
        new_last.next = self.tail

        self.size += other.size

x = Node(16)
y = Node(27)
z = Node(34)

link = LinkedList()
link.insert(x, 0)
link.insert(y, 0)
link.insert(z)
link.display()

link.delete(1)
link.get(1)
link.display()

link.delete()
link.display()

link2 = LinkedList()
a = Node(29)
b = Node(53)
link2.insert(a)
link2.insert(b, 0)
link2.display()

link.concat(link2)
link.display()
