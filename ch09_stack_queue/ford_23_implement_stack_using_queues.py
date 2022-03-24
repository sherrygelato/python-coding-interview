"""
CH09. 23_Implement_Stack_using_Queue.py
"""

# --------------------------------------------------
import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque()
        
        
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())


    def pop(self):
        return self.q.popleft()


    def top(self):
        return self.q[0]


    def emtpy(self):
        return len(self.q) == 0


stack = MyStack()

stack.push(1)
stack.push(2)

stack.top()

stack.pop()
stack.emtpy()