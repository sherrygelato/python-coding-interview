"""
CH19. 70_Single_Number.py
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
input1 = [2, 2, 1]

# 출력 1
output1 = 1


# 입력 2
input2 = [4, 1, 2, 1, 2]

# 출력 2
output2 = 4


# --------------------------------------------------
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


print(singleNumber(input1))
print(singleNumber(input1) == output1)
print(singleNumber(input2))
print(singleNumber(input2) == output2)