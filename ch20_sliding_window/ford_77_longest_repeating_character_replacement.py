"""
CH20. 77_Longest_Repeating_Character_Replacement.py
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
s = 'AAABBC'
k = 2

# 출력
output = 5


# --------------------------------------------------
def characterReplacement(s, k):
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        
        max_char_n = counts.most_common(1)[0][1]
        
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left


print(characterReplacement(s, k))
print(characterReplacement(s, k) == output)
