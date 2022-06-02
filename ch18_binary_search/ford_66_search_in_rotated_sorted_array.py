"""
CH18. 66_Search_in_Rotated_Sorted_Array.py
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
nums = [4, 5, 6, 7, 0, 1, 2]
target = 1

# 출력
output = 5


# --------------------------------------------------
def search(nums, target):
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
             right = mid
            
    pivot = left
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)
        
        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1


print(search(nums, target))
print(search(nums, target) == output)


# --------------------------------------------------
