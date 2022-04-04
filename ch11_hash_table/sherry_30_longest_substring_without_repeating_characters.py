# Python
# -*- coding:UTF-8 -*-

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
# from typing import *

# 문제 30 : 중복 문자가 없는 가장 긴 부분 문자열substring의 길이를 리턴하라.
# 입력
input1 = "abcabcbb" # 출력 :  3
input2 = "bbbbb" # 출력 : 1
input3 = "pwwkew" # 출력 : 3

# 풀이 1 슬라이딩 윈도우와 투 포인터로 사이즈 조절

def lengthOfLongestSubstring(s):
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 start 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start +1)
            
        # 현재 문자의 위치 삽입
        used[char] = index
    
    return max_length

print(lengthOfLongestSubstring(input1))
print(lengthOfLongestSubstring(input2))
print(lengthOfLongestSubstring(input3))