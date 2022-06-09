"""
CH22. 83_Majority_Element.py
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


# 입력 1
nums1 = [3, 2, 3]

# 출력 1
output1 = 3

# 입력 2
nums2 = [2, 2, 1, 1, 1, 2, 2]

# 출력 2
output2 = 2


# --------------------------------------------------
def majorityElement(nums):
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num


print(majorityElement(nums1))
print(majorityElement(nums1) == output1)
print(majorityElement(nums2))
print(majorityElement(nums2) == output2)


# --------------------------------------------------
def majorityElement2(nums):
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)
        
        if counts[num] > len(nums) // 2:
            return num


print(majorityElement2(nums1))
print(majorityElement2(nums1) == output1)
print(majorityElement2(nums2))
print(majorityElement2(nums2) == output2)


# --------------------------------------------------
def majorityElement3(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    a = majorityElement3(nums[:half])
    b = majorityElement3(nums[half:])
    
    return [b, a][nums.count(a) > half]


print(majorityElement3(nums1))
print(majorityElement3(nums1) == output1)
print(majorityElement3(nums2))
print(majorityElement3(nums2) == output2)


# --------------------------------------------------
def majorityElement4(nums):
    return sorted(nums)[len(nums) // 2]


print(majorityElement4(nums1))
print(majorityElement4(nums1) == output1)
print(majorityElement4(nums2))
print(majorityElement4(nums2) == output2)
