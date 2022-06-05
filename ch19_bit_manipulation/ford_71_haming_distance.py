"""
CH19. 71_Hamming_Distance.py
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
x = 1
y = 4

# 출력
output = 2


# --------------------------------------------------
def hammingDistance(x, y):
    print(bin(x^y))
    return bin(x^y).count('1')


print(hammingDistance(x, y))
print(hammingDistance(x, y) == output)
