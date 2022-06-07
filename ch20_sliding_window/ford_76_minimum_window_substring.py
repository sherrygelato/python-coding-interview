"""
CH20. 76_Minimum_Window_Substring.py
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


# 입력
S = "ADOBECODEBANC"
T = "ABC"

# 출력
output = "BANC"


# --------------------------------------------------
def minWindow(s, t):
    def contains(s_substr_lst, t_lst):
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else:
                return False
        return True
    
    if not s or not t:
        return ''
    
    window_size = len(t)
    
    for size in range(window_size, len(s) + 1):
        for left in range(len(s) - size + 1):
            s_substr = s[left:left+size]
            if contains(list(s_substr), list(t)):
                return s_substr
    return ''


print(minWindow(S, T))
print(minWindow(S, T) == output)


# --------------------------------------------------
def minWindow2(s, t):
    need = collections.Counter(t)
    missing = len(t)
    
    left = start = end = 0
    
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1
        
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
                
            if not end or right - left <= end - start:
                start, end = left, right
            
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]


print(minWindow2(S, T))
print(minWindow2(S, T) == output)


# --------------------------------------------------
def minWindow3(s, t):
    t_count = collections.Counter(t)
    current_count = collections.Counter()
    
    start = float('-inf')
    end = float('inf')
    
    left = 0
    for right, char in enumerate(s, 1):
        current_count[char] += 1
        
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            current_count[s[left]] -= 1
            left += 1
        
    return s[start:end] if end - start <= len(s) else ''


print(minWindow3(S, T))
print(minWindow3(S, T) == output)
