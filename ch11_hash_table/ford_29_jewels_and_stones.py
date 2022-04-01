"""
CH10. 29_Jewels_and_Stones.py
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
J = "aA"
S = "aAAbbbb"

# 출력 3

# --------------------------------------------------
def numJewelsInStone(J, S):
    freqs = {}
    count = 0
    
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    for char in J:
        if char in freqs:
            count += freqs[char]

    return count


print(numJewelsInStone(J, S))


# --------------------------------------------------
def numJewelsInStone2(J, S):
    freqs = collections.defaultdict(int)
    count = 0
    
    for char in S:
        freqs[char] += 1

    for char in J:
        count += freqs[char]

    return count


print(numJewelsInStone2(J, S))


# --------------------------------------------------
def numJewelsInStone3(J, S):
    freqs = collections.Counter(S)
    count = 0
    
    for char in J:
        count += freqs[char]

    return count


print(numJewelsInStone3(J, S))


# --------------------------------------------------
def numJewelsInStone4(J, S):
    return sum(s in J for s in S)

print([s for s in S])
print([(s in J) for s in S])
print([s in J for s in S])