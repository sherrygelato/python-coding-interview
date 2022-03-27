# Python
# -*- coding:UTF-8 -*-

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
# from typing import *

# 문제 24 스택을 이용한 큐 구현 : 스택를 이용해 다음 연산을 지원하는 큐를 구현하라.
# - push(x) : 요소 x를 큐 마지막에 삽입한다.
# - pop() : 큐 처음에 있는 요소를 삭제한다.
# - peek() : 큐 처음에 있는 요소를 조회한다.
# - empty() : 큐가 비어 있는지 여부를 리턴한다.

"""
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.pop(); // 1 리턴
queue.peek(); // 1 리턴
queue.empty(); // false 리턴
"""

# 풀이 1 스택 2개 이용
 
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
        # output 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []

queue = MyQueue()

print(queue.push(1))
print(queue.push(2))
print(queue.peek()) # 1 리턴
print(queue.pop()) # 1 리턴
print(queue.empty()) # false 리턴