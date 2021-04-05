# MENGGUNAKAN LIST
alist = [] 
alist.append("A") 
alist.append("B") 
alist.append("C") 
alist.append("D") 
alist.append("E") 
print(alist) # Menampilkan hasil push/append pada list
print(alist.pop()) # Mengambil data paling terakhir pada list keluar dari list
print(alist.pop())
print(alist) # Menampilkan isi list setelah pop 
print(alist[-1]) # Mengambil data dari suatu posisi tanpa menghapusnya

# MENGGUNAKAN DEQUE
from collections import deque
deq = deque()
print(dir(deq)) # Method yang ada pada class deque module collections
deq.append("A")
deq.append("B") 
deq.append("C") 
deq.append("D") 
deq.append("F") 
print(deq) # Menampilkan hasil push/append pada deque
print(deq.pop()) # Mengambil data paling terakhir pada deque keluar dari deque
print(deq.pop())
print(deq) # Menampilkan isi deque setelah pop
    
# IMPLEMENTASI CLASS STACK MENGGUNAKAN DEQUE
class Stack:
    def __init__(self):
        self.container = deque() # Memanggil class deque
    def push(self, val):
        self.container.append(val) # Menambah (append)
    def pop(self): 
        return self.container.pop() # Mengambil data paling terakhir
    def peek(self):
        return self.container[-1] # Menampilkan data paling terakhir
    def is_empty(self):
        return len(self.container)==0 # Melihat jika stack kosong
    def size(self):
        return len(self.container) # Melihat panjang/besar stack
 
s = Stack()
print(s) # Akan menampilkan letak objek pada memori
s.push(5) # Memasukan data ke stack
s.is_empty() # Mengecek apakah data kosong, expected output: False
s.pop() # Mengeluarkan data
s.is_empty() # Mengecek apakah data kosong, expected output: True
s.push(5) 
s.push(6) 
s.push(7) 
s.push(8) 
print(s.peek()) # Menampilkan data yang paling terakhir tanpa menghapus
print(s.pop()) # Mengambil data yang paling terakhir 
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop()) # Expected output: IndexError: pop from an empty deque
