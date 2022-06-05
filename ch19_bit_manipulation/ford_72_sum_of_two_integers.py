"""
CH19. 72_Sum_of_Two_Integers.py
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
a1 = 1
b1 = 2

# 출력 1
output1 = 3


# 입력 2
a2 = -2
b2 = 3

# 출력 2
output2 = 1


# --------------------------------------------------
def getSum(a, b):
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    
    a_bin = bin(a & MASK)[2:].zfill(32)
    b_bin = bin(b & MASK)[2:].zfill(32)
    
    result = []
    carry = 0
    sum = 0
    for i in range(32):
        A = int(a_bin[31 - i])
        B = int(b_bin[31 - i])
        
        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        sum = carry ^ Q2
        carry = Q1 | Q3
        
        result.append(str(sum))
    if carry == 1:
        result.append('1')
    
    result = int(''.join(result[::-1]), 2) & MASK
    
    if result > INT_MAX:
        result = ~(result ^ MASK)
    
    return result

print(getSum(a1, b1))
print(getSum(a1, b1) == output1)
print(getSum(a2, b2))
print(getSum(a2, b2) == output2)


# --------------------------------------------------
def getSum2(a, b):
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    
    if a > INT_MAX:
        a = ~(a ^ MASK)
    return a


print(getSum2(a1, b1))
print(getSum2(a1, b1) == output1)
print(getSum2(a2, b2))
print(getSum2(a2, b2) == output2)