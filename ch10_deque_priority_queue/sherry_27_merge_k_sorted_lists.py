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
from typing import List

# 문제 27 k개 정렬 리스트 병합 : k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.

### # 예제 1
input = '[1->4->5, 1->3->4, 2->6]' # 출력 1->1->2->3->4->4->5->6
k = 3

# 풀이 1 우선순위 큐를 이용한 리스트 병합

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
