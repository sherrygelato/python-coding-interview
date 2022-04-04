"""
CH12. 33_Letter_Combinations_of_a_Phone_Number.py
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
input = "23"

# 출력
output = ['ad', 'ae', 'af', 
          'bd', 'be', 'bf', 
          'cd', 'ce', 'cf']

# --------------------------------------------------
def letterCombinations(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i+1, path+j)

    if not digits:
        return []
            
    dic = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    result = []
    dfs(0, '')
    
    return result

print(letterCombinations(input))
