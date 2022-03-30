"""
CH10. 27_Merge_k_Sorted_Lists.py
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

# 입력
# [
#     1->4->5,
#     1->3->4,
#     2->6
# ]
node11 = ListNode(1)
node12 = ListNode(4)
node13 = ListNode(5)
node11.next = node12
node12.next = node13

node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
node21.next = node22
node22.next = node23

node31 = ListNode(2)
node32 = ListNode(6)
node31.next = node32

lists = [node11, node21, node31]

# 출력: 1->1->2->3->4->4->5->6

# --------------------------------------------------
def mergeKLists(lists):
    root = result = ListNode(None)
    heap = []
    
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
            
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]
        
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    
    return root.next


result = mergeKLists(lists)

while result:
    print(result.val, end = ' ')
    result = result.next