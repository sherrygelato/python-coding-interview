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

# 문제 14 정렬되어 있는 두 연결 리스트를 합쳐라

# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 예제 1 : 1->2->4, 1->3->4

# l1 : 1->2->4
node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# l2 : 1->3->4
node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)

# 입력
l1, l2 = node3, node6  # 1->1->2->3->4->4

# 풀이 1 재귀 구조로 연결 

def mergeTwoLists1(l1, l2):
    # 병합 정렬의 마지막 조합과 동일한 방식으로 첫 번째부터 비교하면서 리턴하는 풀이

    # l1과 l2의 값을 비교해 작은 값이 왼쪽에 오게 함
    # 비교 연산 -> and -> or 순으로 
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1 # swap
    if l1:
        # next는 다음 값이 엮이도록 함(재귀 호출)
        l1.next = mergeTwoLists1(l1.next, l2)

    return l1

# 결과
print(mergeTwoLists1(l1, l2))
