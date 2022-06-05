"""
CH19. 74_Number_of_1_Bits.py
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
data1 = 0b00000000000000000000000000001011

# 출력 1
output1 = 3

# 입력 2
data2 = 0b00000000000000000000000010000000

# 출력 2
output2 = 1

# 입력 3
data3 = 0b11111111111111111111111111111101

# 출력 3
output3 = 31


# --------------------------------------------------
def hammingWeight(n):
    return bin(n ^ 0b00000000000000000000000000000000).count('1')


print(hammingWeight(data1))
print(hammingWeight(data1) == output1)
print(hammingWeight(data2))
print(hammingWeight(data2) == output2)
print(hammingWeight(data3))
print(hammingWeight(data3) == output3)


# --------------------------------------------------
def hammingWeight2(n):
    return bin(n ^ 0).count('1')


print(hammingWeight2(data1))
print(hammingWeight2(data1) == output1)
print(hammingWeight2(data2))
print(hammingWeight2(data2) == output2)
print(hammingWeight2(data3))
print(hammingWeight2(data3) == output3)


# --------------------------------------------------
def hammingWeight3(n):
    return bin(n).count('1')


print(hammingWeight3(data1))
print(hammingWeight3(data1) == output1)
print(hammingWeight3(data2))
print(hammingWeight3(data2) == output2)
print(hammingWeight3(data3))
print(hammingWeight3(data3) == output3)


# --------------------------------------------------
def hammingWeight4(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


print(hammingWeight4(data1))
print(hammingWeight4(data1) == output1)
print(hammingWeight4(data2))
print(hammingWeight4(data2) == output2)
print(hammingWeight4(data3))
print(hammingWeight4(data3) == output3)