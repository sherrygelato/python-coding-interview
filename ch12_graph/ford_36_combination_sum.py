"""
CH12. 36_Combination_Sum.py
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
candidates = [2,3,6,7]
target = 7

# 출력 1
output = [
    [2,2,3],
    [7]
]

# 입력 2
candidates2 = [2,3,5]
target2 = 8

# 출력 2
output2 = [
    [2,2,2,2],
    [2,3,3],
    [3,5]
]

# --------------------------------------------------
def combinationSum(candidates, target):
    result = []
    
    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])
    
    dfs(target, 0, [])
    return result


print(combinationSum(candidates, target))
print(combinationSum(candidates, target) == output)
print(combinationSum(candidates2, target2))
print(combinationSum(candidates2, target2) == output2)


# --------------------------------------------------
def permutationSum2(candidates, target):
    result = []
    
    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], 0, path + [candidates[i]])
    
    dfs(target, 0, [])
    return result


print(permutationSum2(candidates, target))
print(permutationSum2(candidates2, target2))