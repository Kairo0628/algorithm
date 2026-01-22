class Queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.is_empty():
            raise ValueError()
        return self.queue[0]
    
    def enqueue(self, n):
        self.queue.append(n)
    
    def dequeue(self):
        return self.queue.pop(0)
    
class CircularQueue():
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def is_full(self):
        return self.size == len(self.queue)
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[(self.front + 1) % len(self.queue)]

    def enqueue(self, n):
        if self.is_full():
            raise ValueError()
        
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = n
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        self.front = (self.front + 1) % len(self.queue)
        self.queue[self.front], pop = None, self.queue[self.front]
        self.size -= 1

        return pop