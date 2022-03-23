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
from typing import *

# 문제 15 역순 연결 리스트 : 연결 리스트를 뒤집어라.

# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next

# 예제 1 : 1->2->3->4->5->Null
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# 입력
head = node1  # 5->4->3->2->1->NULL

# 풀이 1 재귀 구조로 뒤집기 Recursive

def reverseList1(head):
    def reverse(node, prev):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head, next)

# 결과
# printLinkedList(reverseList1(head))

# 풀이 2 반복 구조로 뒤집기

def reverseList2(head):
    node, prev = head, None
    while node:
        # node.next를 prev로 계속 연결하면서 끝날 때까지 반복함
        # node가 None이 될 때 prev는 뒤집힌 연결 리스트의 첫번째 노드가 됨
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# 결과
printLinkedList(reverseList2(head))
# print(reverseList2(head))
