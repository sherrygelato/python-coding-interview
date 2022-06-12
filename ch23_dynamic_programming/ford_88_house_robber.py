"""
CH23. 88_House_Robber.py
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
input1 = [1, 2, 3, 1]

# 출력 1
output1 = 4


# 입력 2
input2 = [2, 7, 9, 3, 1]

# 출력 2
output2 = 12


# 입력 3
input3 = [8, 7, 3, 9]

# 출력 3
output3 = 17


# 입력 4
input4 = [9, 3, 9, 8]

# 출력 4
output4 = 18


# --------------------------------------------------
def rob(nums):
    def _rob(i):
        if i < 0:
            return 0
        return max(_rob(i - 1), _rob(i - 2) + nums[i])
    return _rob(len(nums) - 1)


print(rob(input1))
print(rob(input1) == output1)
print(rob(input2))
print(rob(input2) == output2)
print(rob(input3))
print(rob(input3) == output3)
print(rob(input4))
print(rob(input4) == output4)


# --------------------------------------------------
def rob1(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
    return dp.popitem()[1]


print(rob1(input1))
print(rob1(input1) == output1)
print(rob1(input2))
print(rob1(input2) == output2)
print(rob1(input3))
print(rob1(input3) == output3)
print(rob1(input4))
print(rob1(input4) == output4)
