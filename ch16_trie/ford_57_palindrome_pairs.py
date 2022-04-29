"""
CH16. 57_Palindrome_Pairs.py
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
input1 = ['abcd', 'dcba', 'lls', 's', 'sssll']
# 출력 1
output1 = [[0,1], [1,0], [3,2], [2,4]]

# 입력 2 
input2 = ['bat', 'tab', 'cat']
# 출력 2
output2 = [[0,1], [1,0]]

# 입력 3 
input3 = ['d', 'cbbcd', 'dcbb', 'dcbc', 'cbbc', 'bbcd']
# 출력 3
output3 = [[0,1], [1,0]]


# --------------------------------------------------
def palindromePairs(words):
    def is_palindrome(word):
        return word == word[::-1]
    
    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
    return output


print(palindromePairs(input1))
print(palindromePairs(input1) == output1)
print(palindromePairs(input2))
print(palindromePairs(input2) == output2)
print(palindromePairs(input3))
print(palindromePairs(input3) == output3)


# --------------------------------------------------
