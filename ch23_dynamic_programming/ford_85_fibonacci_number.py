"""
CH23. 85_Fibonacci_Number.py
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
input1 = 5

# 출력
output1 = 5

# 입력 2
input2 = 10

# 출력 2
output2 = 55


# --------------------------------------------------
def fib(N):
    if N <= 1:
        return N
    return fib(N-1) + fib(N-2)


print(fib(input1))
print(fib(input1) == output1)
print(fib(input2))
print(fib(input2) == output2)


# --------------------------------------------------
dp = collections.defaultdict(int)
def fib2(N):
    global dp
    if N <= 1:
        return N
    
    if dp[N]:
        return dp[N]
    dp[N] = fib2(N-1) + fib2(N-2)
    return dp[N]


print(fib2(input1))
print(fib2(input1) == output1)
print(fib2(input2))
print(fib2(input2) == output2)


# --------------------------------------------------
class Solution:
    dp = collections.defaultdict(int)
    
    def fib2_1(self, N):
        if N <= 1:
            return N
        
        if self.dp[N]:
            return self.dp[N]
        
        self.dp[N] = self.fib2_1(N-1) + self.fib2_1(N-2)
        return self.dp[N]
        
sol = Solution()

print(sol.fib2_1(input1))
print(sol.fib2_1(input1) == output1)
print(sol.fib2_1(input2))
print(sol.fib2_1(input2) == output2)


# --------------------------------------------------
dp = collections.defaultdict(int)
def fib3(N):
    global dp
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, N + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]


print(fib3(input1))
print(fib3(input1) == output1)
print(fib3(input2))
print(fib3(input2) == output2)


# --------------------------------------------------
class Solution:
    dp = collections.defaultdict(int)
    
    def fib3_1(self, N):
        self.dp[0] = 0
        self.dp[1] = 1
        
        for i in range(2, N+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[N]
    

sol = Solution()

print(sol.fib3_1(input1))
print(sol.fib3_1(input1) == output1)
print(sol.fib3_1(input2))
print(sol.fib3_1(input2) == output2)


# --------------------------------------------------
def fib4(N):
    x, y = 0, 1
    for i in range(2, N+1):
        x, y = y, x+y
    return y


print(fib4(input1))
print(fib4(input1) == output1)
print(fib4(input2))
print(fib4(input2) == output2)


# --------------------------------------------------
import numpy as np

def fib5(N):
    M = np.matrix([[0, 1], [1, 1]])
    print(M)
    vec = np.array([[0], [1]])
    
    return np.matmul(M ** N, vec)[0]


print(fib5(input1))
print(fib5(input1) == output1)
print(fib5(input2))
print(fib5(input2) == output2)

