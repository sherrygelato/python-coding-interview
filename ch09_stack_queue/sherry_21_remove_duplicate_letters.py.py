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
from typing import *

# 문제 21 중복 문자 제거 : 중복된 문자를 제외하고 사전식 순서 Lexicographical Order로 나열하라.

# 예제 
input1 = "bcabc" # 출력 "abc"
input2 = "cbacdcbc" # 출력 "acdb"

# 풀이 1 재귀를 이용한 분리
 
def removeDuplicateLetters1(s):
    # 집합으로 정렬 : 중복 문자 제외
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할때 분리 진행
        if set(s) == set(suffix):
            # 재귀호출 구조로 일종의 분할 정복과 비슷한 형태로 더 이상 남지 않을 때 결과가 조합됨ㄴ
            return char + removeDuplicateLetters1(suffix.replace(char, ''))
    return ''

print(removeDuplicateLetters1(input1))
print(removeDuplicateLetters1(input2))

# 풀이 2 스택을 이용한 문자 제거

def removeDuplicateLetters2(s):
    # 스택을 이용해서 중복 문자 제거를 할 수 있다.
    counter, seen, stack = collections.Counter(s), set(), []
    # collections.Counter() : 문자별 개수를 자동으로 카운팅

    for char in s:
        counter[char] -= 1
        if char in seen:
            # seen : 집합 set의 자료형, 이미 처리된 문자 여부를 확인하는데, 이미 저리된 문자는 스킵한다.
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)

print(removeDuplicateLetters2(input1))
print(removeDuplicateLetters2(input2))