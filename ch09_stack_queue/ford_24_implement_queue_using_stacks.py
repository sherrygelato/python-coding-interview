"""
CH09. 24_Implement_Queue_using_Stack.py
"""

# --------------------------------------------------
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []


    def push(self, x):
        self.input.append(x)


    def pop(self):
        self.peek()
        return self.output.pop()


    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]


    def empty(self):
        return self.input == [] and self.output == []


queue = MyQueue()

queue.push(1)
queue.push(2)

queue.peek()

queue.pop()

queue.empty()