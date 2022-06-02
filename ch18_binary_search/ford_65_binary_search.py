"""
CH18. 65_Binary_Search.py
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
nums = [-1, 0, 3, 5, 9, 12]
target = 9

# 출력
output = 4


# --------------------------------------------------
def search(nums, target):
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                return binary_search(mid+1, right)
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else:
                return mid
        else:
            return -1
        
    return binary_search(0, len(nums) - 1)


print(search(nums, target))
print(search(nums, target) == output)


# --------------------------------------------------
def search2(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


print(search2(nums, target))
print(search2(nums, target) == output)


# --------------------------------------------------
def search3(nums, target):
    index = bisect.bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1


print(search3(nums, target))
print(search3(nums, target) == output)


# --------------------------------------------------
def search4(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1


print(search4(nums, target))
print(search4(nums, target) == output)


# --------------------------------------------------
def search5(nums, target):
    def binary_search(left, right):
        if left <= right:
            mid = left + (right-left) // 2
            
            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1
        
    return binary_search(0, len(nums) - 1)


print(search5(nums, target))
print(search5(nums, target) == output)