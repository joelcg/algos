from collections import deque

class Stack:
    def __init__(self):
        self.container = deque() 
    def push(self, val):
        self.container.append(val) 
    def pop(self): 
        return self.container.pop() 
    def peek(self):
        return self.container[-1] 
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container) 
    
    # 1. FUNGSI REVERSE STRING
    def reverse_string(self, string):
        reversed = ""
        for x in range(len(string)):
            self.push(string[x])
        for x in range(len(string)):
            reversed += self.pop()
        return reversed
    
    # 2. FUNGSI PENGECEKAN TANDA KURUNG SEIMBANG
    def is_right(self, a, b): # Ini adalah fungsi pembandingannya (terpisah; agar biar mudah dibaca)
        if a == "(" and b == ")":
            return True
        elif a == "[" and b == "]":
            return True
        elif a == "{" and b == "}":
            return True
        else:
            return False

    def is_balanced(self, string):
        opening = ["(","[","{"] 
        closing = [")","]","}"]
        for x in string:
            if x in opening:
                self.push(x)
            if x in closing:
                if self.is_empty():
                    return False
                else:
                    if self.is_right(self.peek(), x):
                        self.pop()
        if self.is_empty():
            return True
        else:
            return False

test = Stack()
# 1. FUNGSI REVERSE STRING
print(test.reverse_string("Bebas dari COVID-19 kita sehat semua!"))
# 2. FUNGSI PENGECEKAN TANDA KURUNG SEIMBANG
print(test.is_balanced("({a+b})")) 
print(test.is_balanced("))((a+b)("))
print(test.is_balanced("((a+b))"))
print(test.is_balanced("))"))
print(test.is_balanced("[a+b]*(x+2y)*{gg+kk}")) 
    