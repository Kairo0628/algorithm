class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head
    
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
        
        mid = self.size // 2

        if index <= mid:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr
    
    def insert(self, node: Node, index = None):
        if index == None:
            index = self.size

        if index > self.size or index < 0:
            raise IndexError()
        
        prev = self.get(index - 1)
        next = prev.next

        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

        self.size += 1

    def delete(self, index = None):
        if index == None:
            index = self.size - 1

        if index > self.size - 1 or index < 0:
            raise IndexError()
        
        curr = self.get(index)
        prev = curr.prev
        next = curr.next

        prev.next = next
        next.prev = prev

        self.size -= 1

        return curr
    
    def concat(self, other: 'DoublyLinkedList'):
        if other.size == 0:
            return

        curr_last = self.tail.prev
        other_first = other.head.next

        curr_last.next = other_first
        other_first.prev = curr_last
        self.tail = other.tail

        self.size += other.size

link1 = DoublyLinkedList()
n1 = Node(16)
n2 = Node(37)
n3 = Node(67)

link1.insert(n1)
link1.insert(n2, 1)
link1.insert(n3, 1)
link1.display()

link1.delete(1)
link1.display()

link2 = DoublyLinkedList()
x1 = Node(22)
x2 = Node(54)

link2.insert(x1)
link2.insert(x2)
link2.display()

link2.delete()
link2.display()

link1.concat(link2)
link1.display()
