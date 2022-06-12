"""
CH23. 86_Maximum_Subarray.py
"""

import collections
import enum
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력
input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# 출력
output = 6


# --------------------------------------------------
def maxSubArray0(nums):
    sums = [nums[0]]
    for i in range(1, len(nums)):
        sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
    return max(sums)


print(maxSubArray0(input))
print(maxSubArray0(input) == output)


# --------------------------------------------------
def maxSubArray(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
    return max(nums)


result = maxSubArray(input)
print(result)
print(result == output)


# --------------------------------------------------
input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubArray1(nums):
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    
    return best_sum


print(maxSubArray1(input))
print(maxSubArray1(input) == output)
