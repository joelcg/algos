from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

def binary(x):
    qu = Queue()
    qu.enqueue("1")
    for i in range(x):
        print(qu.front())
        qu.enqueue(qu.front() + "0")
        qu.enqueue(qu.front() + "1")
        qu.dequeue()
        
binary(10)
        