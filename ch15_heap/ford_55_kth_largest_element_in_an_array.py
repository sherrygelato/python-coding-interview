"""
CH15. 55_Kth_Largetst_Element_in_an_Array.py
"""
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력 1 
input = [3,2,1,2,4,5,5,6]
k = 4
# 출력 1
output = 4


# --------------------------------------------------
def findKthLargest(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
        
    for _ in range(1, k):
        heapq.heappop(heap)
        
    return -heapq.heappop(heap)


print(findKthLargest(input, k))
print(findKthLargest(input, k) == output)


# --------------------------------------------------
def findKthLargest2(nums, k):
    heapq.heapify(nums)
    
    for _ in range(len(nums) - k):
        heapq.heappop(nums)
        
    return heapq.heappop(nums)


print(findKthLargest2(input, k))
print(findKthLargest2(input, k) == output)


# --------------------------------------------------
def findKthLargest3(nums, k):
    return heapq.nlargest(k, nums)[-1]


print(findKthLargest3(input, k))
print(findKthLargest3(input, k) == output)


# --------------------------------------------------
def findKthLargest4(nums, k):
    return sorted(nums, reverse=True)[k-1]


print(findKthLargest4(input, k))
print(findKthLargest4(input, k) == output)
