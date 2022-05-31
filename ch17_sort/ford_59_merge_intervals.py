"""
CH17. 59_Merge_Intervals.py
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
input = [[1,3], [2,6], [8,10], [15,18]]

# 출력
output = [[1,6], [8,10], [15,18]]

# --------------------------------------------------
def merge(intervals):
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += i,
    return merged


print(merge(input))
print(merge(input) == output)
