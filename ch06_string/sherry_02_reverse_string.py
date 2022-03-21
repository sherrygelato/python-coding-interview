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

class Solution:

    # 문제 02 문자열 뒤집기 : 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

    # 예제
    s21 = ["h", "e", "l", "l", "o"] # ["o","l","l","e","h"]
    s22 = ["H", "a", "n", "n", "a", "h"] # ["h","a","n",*'n'*,"a","H"]

    # 풀이 1 투 포인터를 이용한 스왑
    def reverseString1(s): 
        # 투 포인터 Two Pointer는 단어 그대로 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
        # 리턴 없이 리스트 내부를 직접 조작, s 내부를 스왑하는 형태로 풀이
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # 풀이 2 파이썬다운 방식
    def reverseString2(s): 
        # Pythonic way, 파이썬의 기본 기능으로 단 한 줄로 풀이
        s.reverse()
        # reverse()는 리스트에만 제공, 입력값이 문자열이라면 문자열 슬라이싱을 사용할 수 있고, 성능 또한 좋음
    
    # 결과
    print(reverseString1(s21))
    print(reverseString1(s22))
    print(reverseString2(s21))
    print(reverseString2(s22))