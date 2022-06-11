"""
CH23. 87_Climbing_Stairs.py
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
input = 3

# 출력
output = 3


# --------------------------------------------------
def climbingStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbingStairs(n - 1) + climbingStairs(n - 2)


print(climbingStairs(input))
print(climbingStairs(input) == output)


# --------------------------------------------------
class Solution:
    dp = collections.defaultdict(int)
    
    def climbingStairs(self, n):
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbingStairs(n - 1) + self.climbingStairs(n - 2)
        return self.dp[n]


sol = Solution()
print(sol.climbingStairs(input))
print(sol.climbingStairs(input) == output)
