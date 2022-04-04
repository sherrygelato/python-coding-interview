"""
CH11. 31_Top_K_Frequent_Element.py
"""
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect

# 입력
nums = [1,1,1,2,2,3]
k = 2

# 출력
# [1, 2]

# --------------------------------------------------
def topKFrequent(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    
    return topk


print(topKFrequent(nums, k))


# --------------------------------------------------
def topKFrequent2(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


print(topKFrequent2(nums, k))
