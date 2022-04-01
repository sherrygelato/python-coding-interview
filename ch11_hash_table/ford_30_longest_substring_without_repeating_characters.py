"""
CH10. 30_Longest_Substring_Without_Repeating_Characters.py
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
str1 = "abcabcbb"

# 출력 1
# 3


# 입력 2
str2 = "bbbbb"

# 출력 2
# 1


# 입력 3
str3 = "pwwkew"

# 출력 3
# 1

# --------------------------------------------------
def lengthOfLongestSubstring(s):
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        print(' '*start+'.')
        print(s)
        print(' '*index+'^')
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start +1)
            
        used[char] = index
        print(max_length)
    
    return max_length


print(lengthOfLongestSubstring(str1))
print(lengthOfLongestSubstring(str2))
print(lengthOfLongestSubstring(str3))


# --------------------------------------------------