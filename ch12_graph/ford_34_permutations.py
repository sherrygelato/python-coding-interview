"""
CH12. 34_Permutations.py
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
input = [1,2,3]

# 출력
output = [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
]

# --------------------------------------------------
def permute(nums):
    results = []
    prev_elements = []
    
    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])
        
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
            
    dfs(nums)
    return results


print(permute(input))
print(permute(input) == output)


# --------------------------------------------------
def permute2(nums):
    return list(itertools.permutations(nums))


print(permute2(input))
print(permute2(input) == output)  # Tuple


# --------------------------------------------------
def permute3(nums):
    return list(map(list, itertools.permutations(nums)))


print(permute3(input))
print(permute3(input) == output)


# --------------------------------------------------
