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

# 문제 26 원형 데크 디자인 : 다음 연산을 제공하는 원형 데크를 디자인하라.
"""
- MyCircularDeque(k): 데크 사이즈를 k로 지정하는 생성자다.
- insertFront(): 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴한다.
- insertLast() 데크 마지막에 아이템을 추가하고 성공할 경우 true를 리턴한다.
- deleteFront(): 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
- deleteLast(): 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
- getFront( ) 데크의 번째 아이템을 가져온다. 데크가 비어 있다면 -1 리턴한다.
- getRear(): 데크의 마지막 아이템을 가져온다. 데크가 비어 있다면 -1 리턴한다.
- isEmpty(): 데크가 비어 있는지 여부를 판별한다.
- isFull( ) 데크가 가득 있는지 여부를 판별한다.
"""

# 풀이 1 이중 연결 리스트를 이용한 데크 구현

# 원형 데크를 디자인 문제. 

# inserFront() : 일반적인 배열로는 맨 앞에 요소를 추가하는 작업은 시간 복잡도가 O(n)이기 때문에 구현이 쉽지 않다.
# 그러나 연결 리스트는 맨 앞에 노드를 추가하는 작업이 어렵지 않다.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyCircularDeque:
    def __init__(self, k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self):
        return self.head.right.val if self.len else -1

    def getRear(self):
        return self.tail.left.val if self.len else -1

    def isEmpty(self):
        return self.len == 0

    def isFull(self):
        return self.len == self.k

