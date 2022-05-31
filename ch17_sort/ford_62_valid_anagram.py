"""
CH17. 62_Valid_Anagram.py
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
s1 = "anagram"
t1 = "nagaram"

# 출력 1
output1 = True


# 입력 2
s2 = "rat"
t2 = "car"

# 출력 2
output2 = False


# --------------------------------------------------
def isAnagram(s, t):
    return sorted(s) == sorted(t)


print(isAnagram(s1, t1))
print(isAnagram(s1, t1) == output1)
print(isAnagram(s2, t2))
print(isAnagram(s2, t2) == output2)
