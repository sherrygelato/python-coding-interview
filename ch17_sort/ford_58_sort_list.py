"""
CH17. 58_Sort_List.py
"""

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def print_node(node):
    while node.next:
        print(node.val)
        node = node.next
    print(node.val)

# 입력 1
# 4 -> 2 -> 1 -> 3
node11 = ListNode(4)
node12 = ListNode(2)
node13 = ListNode(1)
node14 = ListNode(3)
node11.next = node12
node12.next = node13
node13.next = node14

# 출력 1
# 1 -> 2 -> 3 -> 4
node21 = ListNode(1)
node22 = ListNode(2)
node23 = ListNode(3)
node24 = ListNode(4)
node21.next = node22
node22.next = node23
node23.next = node24

# 입력 2
# -1 -> 5 -> 3 -> 4 -> 0
node31 = ListNode(-1)
node32 = ListNode(5)
node33 = ListNode(3)
node34 = ListNode(4)
node35 = ListNode(0)
node31.next = node32
node32.next = node33
node33.next = node34
node34.next = node35


# 출력 2
# -1 -> 0 -> 3 -> 4 -> 5
node41 = ListNode(-1)
node42 = ListNode(0)
node43 = ListNode(3)
node44 = ListNode(4)
node45 = ListNode(5)
node41.next = node42
node42.next = node43
node43.next = node44
node44.next = node45

# --------------------------------------------------
def mergeTwoLists(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = mergeTwoLists(l1.next, l2)
    return l1 or l2

def sortList(head):
    if not(head and head.next):
        return head
    
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    # 분할 재귀 호출
    l1 = sortList(head)
    l2 = sortList(slow)
    
    return mergeTwoLists(l1, l2)


sortList(node11)
print_node(node13)
print_node(node21)
sortList(node31)
print_node(node31)
print_node(node41)


# --------------------------------------------------
def sortList2(head):
    p = head
    lst = []
    while p:
        lst.append(p.val)
        p = p.next
    
    lst.sort()
    
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next
    return head


sortList2(node11)
print_node(node13)
print_node(node21)
sortList2(node31)
print_node(node31)
print_node(node41)
