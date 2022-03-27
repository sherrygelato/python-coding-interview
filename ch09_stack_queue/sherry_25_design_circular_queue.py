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

# 문제 25 원형 큐 디자인 : 원형 큐를 디자인하라.

"""
MyCircularQueue circularQueue = new MyCircularQueue(5); // 크기를 5로지정

ctrcularQueue.enQueue(10); // true 리턴
circularQueue.enQueue(20); // true 리턴
ctrcularQueue.enQueue(30); // true 리턴
circularQueue.enQueue(40); // true 리턴
circularQueue.Rear(); // 40 리턴
circularQueue.isFull(); // false 리턴
circularQueue.deQueue(); // true 리턴
circularQueue.deQueue(); // true 리턴
ctrcularQueue.enQueue(50); // true 리턴
circularQueue.enQueue(60); // true 리턴
circularQueue.Rear(); // 60 리턴
circularQueue.Front(); // 30 리턴
"""

# 풀이 1 배열을 이용한 풀이

class MyCircularQueue:
    # 배열로 구현했을 때 공간을 재활용한다는 원형의 이점을 내세울 수 있다.
    def __init__(self, k):
        # 큐의 크기를 초기화 시 입력받는다. 
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # front 포인터
        self.p2 = 0 # rear 포인터

    # enQueue(): 리어 포인터 이동
    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue(): 프론트 포인터 이동
    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None

circularQueue = MyCircularQueue(5)

print(circularQueue.enQueue(10)) # true 리턴
print(circularQueue.enQueue(20)) # true 리턴
print(circularQueue.enQueue(30)) # true 리턴
print(circularQueue.enQueue(40)) # true 리턴
print(circularQueue.Rear()) # 40 리턴
print(circularQueue.isFull()) # false 리턴
print(circularQueue.deQueue()) # true 리턴
print(circularQueue.deQueue()) # true 리턴
print(circularQueue.enQueue(50)) # true 리턴
print(circularQueue.enQueue(60)) # true 리턴
print(circularQueue.Rear()) # 60 리턴
print(circularQueue.Front()) # 30 리턴