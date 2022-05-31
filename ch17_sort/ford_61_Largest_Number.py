"""
CH17. 61_Largest_Number.py
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
input1 = [10, 2]

# 출력 1
output1 = "210"


# 입력 2
input2 = [3, 30, 34, 5, 9]

# 출력 2
output2 = "9534330"


# --------------------------------------------------
def to_swap(n1, n2):
    return str(n1) + str(n2) < str(n2) + str(n1)

def largestNumber(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and to_swap(nums[j-1], nums[j]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1
    
    return str(int(''.join(map(str, nums))))


print(largestNumber(input1))
print(largestNumber(input1) == output1)
print(largestNumber(input2))
print(largestNumber(input2) == output2)
