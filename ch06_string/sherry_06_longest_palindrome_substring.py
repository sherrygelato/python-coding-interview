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
# from typing import Deque

# 문제 06 가장 긴 팰린드롬 부분 문자열 : 가장 긴 팰린드롬 부분 문자열을 출력하라.

# 예제
s61 = "babad" # "bab", "aba"
s62 = "cbbd" # "bb"

# 풀이 1 : 중앙을 중심으로 확장하는 풀이
def longstPalindrome(s):
    # 팰린드롬 판별한 뒤, 매칭이 될 때 중앙을 중심으로 점점 확장해 나가면서 가장 긴 팰린드롬을 판별하는 알고리즘
    # 2칸, 3칸으로 구성된 투 포인터가 슬라이딩 윈도우처럼 계속 앞으로 전진해 나감
    # 문자열이 팰린드롬인 경우 그 자리에 멈추고, 투 포인터가 점점 확장하는 방식 (짝, 홀수)

    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]
    
    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(0, len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        # expand()로 정의한 중첩 함수에서 홀, 짝수 2개의 투 포인터가 팰린드롬 여부 판별 및 이동
    
    return result


# 결과
print(longstPalindrome(s61))
print(longstPalindrome(s62))
