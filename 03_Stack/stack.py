class Stack:
    def __init__(self, max_len):
        self.stack = []
        self.max_len = max_len
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.max_len
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
        
    def push(self, item):
        if self.is_full():
            raise ValueError()
        else:
            self.stack.append(item)
            self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise ValueError()
        else:
            self.size -= 1
            return self.stack.pop()
        
    def display(self):
        print(self.stack[::-1])
