harga_saham_hmsp_queue = [] #list
harga_saham_hmsp_queue.insert(0, 1355.00)
harga_saham_hmsp_queue.insert(0, 1375.00)
harga_saham_hmsp_queue.insert(0, 1360.00)
print(harga_saham_hmsp_queue)
print(harga_saham_hmsp_queue.pop())
print(harga_saham_hmsp_queue)
print(harga_saham_hmsp_queue.pop())
print(harga_saham_hmsp_queue.pop())
#print(harga_saham_hmsp_queue.pop()) # Ini akan error, karena list kosong

# Penerapan queue dengan collections deque
from collections import deque
q = deque()
q.appendleft(5000)
print(q)
q.appendleft(5200)
q.appendleft(5300)
print(q)
s = deque()
s.append(5000)
s.append(5200)
s.append(5300)
print(s)
print(q.pop())
print(q)
print(s.pop())
print(s)
print(q.pop())
print(q.pop())
#print(q.pop())  # Ini akan error, karena queue kosong

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
    
pq = Queue()
pq.enqueue({
    'company': 'PT Hanjaya',
    'timestamp': '31 Maret, 10.01 AM',
    'price': 1365.00})
pq.enqueue({
    'company': 'PT Hanjaya',
    'timestamp': '31 Maret, 10.03 AM',
    'price': 1360.00})
pq.enqueue({
    'company': 'PT Hanjaya',
    'timestamp': '31 Maret, 10.06 AM',
    'price': 1355.00})
print(pq.size())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
#print(pq.dequeue()) # Ini akan error, karena queue kosong

    