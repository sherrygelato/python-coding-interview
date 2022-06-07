"""
CH20. 75_Sliding_Window_Maximum.py
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
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# 출력
output = [3, 3, 5, 5, 6, 7]


# --------------------------------------------------
def maxSlidingWindow(nums, k):
    if not nums:
        return nums
    
    r = []
    for i in range(len(nums) - k + 1):
        r.append(max(nums[i:i+k]))
    
    return r


print(maxSlidingWindow(nums, k))
print(maxSlidingWindow(nums, k) == output)


# --------------------------------------------------
def maxSlidingWindow2(nums, k):
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue
        
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)
        
        if current_max == window.popleft():
            current_max = float('-inf')
    
    return results


print(maxSlidingWindow2(nums, k))
print(maxSlidingWindow2(nums, k) == output)


# --------------------------------------------------
