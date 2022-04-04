"""
CH12. 35_Combinations.py
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
n = 4
k = 2

# 출력
output = [
    [1,2],
    [1,3],
    [1,4],
    [2,3],
    [2,4],
    [3,4]
]

# --------------------------------------------------
def combine(n, k):
    results = []
    
    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            return
        
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
    
    dfs([], 1, k)
    return results


print(combine(n, k))
print(combine(n, k) == output)


# --------------------------------------------------
def combine2(n, k):
    return list(itertools.combinations(range(1, n + 1), k))


print(combine2(n, k))
print(combine2(n, k) == output)
# --------------------------------------------------
def combine3(n, k):
    return list(map(list, itertools.combinations(range(1, n+1), k)))


print(combine3(n, k))
print(combine3(n, k) == output)