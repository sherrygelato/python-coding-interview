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

# 문제 23 큐를 이용한 스택 구현 : 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
# - push(x) : 요소 x를 스택에 삽입한다.
# - pop() : 스택의 첫 번째 요소를 삭제한다.
# - top() : 스택의 첫 번째 요소를 가져온다.
# - empty() : 스택이 비어 있는지 여부를 리턴한다.

"""
Mystack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top(); // 2 리턴
stack.pop(); // 2 리턴
stack.empty(); // false 리턴
"""

# 풀이 1 push() 할 때 큐를 이용해 재정렬

class MyStack:
    def __init__(self):
        # 데크로 큐 선언
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 방금 삽입한 요소를 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
            # 큐에서 맨 앞 요소를 끄집어낼 때 스택처럼 가장 먼저 삽입한 요소가 나온다.

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

stack = MyStack()

print(stack.push(1))
print(stack.push(2))
print(stack.top()) # 2 리턴
print(stack.pop()) # 2 리턴
print(stack.empty()) # false 리턴