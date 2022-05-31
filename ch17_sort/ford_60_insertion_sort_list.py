"""
CH17. 60_Insertion_Sort_List.py
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


# 입력
# 4 -> 2 -> 1 -> 3
node11 = ListNode(4)
node12 = ListNode(2)
node13 = ListNode(1)
node14 = ListNode(3)
node11.next = node12
node12.next = node13
node13.next = node14

# 출력
# 1 -> 2 -> 3 -> 4
node21 = ListNode(1)
node22 = ListNode(2)
node23 = ListNode(3)
node24 = ListNode(4)
node21.next = node22
node22.next = node23
node23.next = node24

# --------------------------------------------------
def insertionSortList(head):
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        
        cur.next, head.next, head = head, cur.next, head.next
        
        cur = parent
    return cur.next

insertionSortList(node11)
print_node(node13)
print_node(node21)


# --------------------------------------------------
def insertionSortList2(head):
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next
        
        if head and cur.val > head.val:
            cur = parent
    return parent.next

insertionSortList2(node11)
print_node(node13)
print_node(node21)
