"""
CH21. 82_Assign_Cookies.py
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
child1 = [1, 2, 3]
cookie1 = [1, 1]

# 출력 1
output1 = 1

# 입력 2
child2 = [1, 2]
cookie2 = [1, 2, 3]

# 출력 2
output2 = 2


# --------------------------------------------------
def findContentChildren(g, s):
    g.sort()
    s.sort()
    
    child_i = cookie_j = 0
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
        
    return child_i


print(findContentChildren(child1, cookie1))
print(findContentChildren(child1, cookie1) == output1)
print(findContentChildren(child2, cookie2))
print(findContentChildren(child2, cookie2) == output2)


# --------------------------------------------------
def findContentChildren2(g, s):
    g.sort()
    s.sort()
    
    result = 0
    for i in s:
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    return result


print(findContentChildren2(child1, cookie1))
print(findContentChildren2(child1, cookie1) == output1)
print(findContentChildren2(child2, cookie2))
print(findContentChildren2(child2, cookie2) == output2)
