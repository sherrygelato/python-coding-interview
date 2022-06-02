"""
CH18. 67_Intersection_of_Two_Arrays.py
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
nums11 = [1, 2, 2, 1]
nums12 = [2, 2]

# 출력 1
output1 = {2}

# 입력 2
nums21 = [4, 9, 5]
nums22 = [9, 4, 9, 8, 4]

# 출력 2
output2 = {9, 4}


# --------------------------------------------------
def intersection(nums1, nums2):
    result = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return result


print(intersection(nums11, nums12))
print(intersection(nums11, nums12) == output1)
print(intersection(nums21, nums22))
print(intersection(nums21, nums22) == output2)


# --------------------------------------------------
def intersection2(nums1, nums2):
    result = set()
    nums2.sort()
    for n1 in nums1:
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
    
    return result


print(intersection2(nums11, nums12))
print(intersection2(nums11, nums12) == output1)
print(intersection2(nums21, nums22))
print(intersection2(nums21, nums22) == output2)


# --------------------------------------------------
def intersection3(nums1, nums2):
    result = set()
    nums1.sort()
    nums2.sort()
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    
    return result


print(intersection3(nums11, nums12))
print(intersection3(nums11, nums12) == output1)
print(intersection3(nums21, nums22))
print(intersection3(nums21, nums22) == output2)
