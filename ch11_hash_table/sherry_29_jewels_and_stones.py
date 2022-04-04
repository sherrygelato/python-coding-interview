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

# 문제 29 보석과 돌 : J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 나올까? 대소문자는 구분한다.
# 입력
J = "aA"
S = "aAAbbbb"
# 출력 3

# 풀이 1 해시 테이블을 이용한 풀이
# 갖고 있는 돌 S의 개수를 헤아리고, J의 각 요소를 키로 하는 각 개수를 합산

def numJewelsInStone(J, S):
    freqs = {}
    count = 0
    
    # 돌의 모음인 S를 문자 단위로 하나씩 분리해 반족한다.
    for char in S:
        if char not in freqs:
            freqs[char] = 1 # 처음 등장한 문자의 경우
            print("freqs1 : ", freqs)
        else:
            freqs[char] += 1 # 기존에 있던 문자의 경우
            print("freqs2 : ", freqs)

    for char in J:
        if char in freqs:
            # 해당 문자 빈도수 더하기
            count += freqs[char]

    return count

print(numJewelsInStone(J, S))

# 풀이 2 defaultdict을 이용한 비교 생략
# defaultdict을 사용해 존재하지 않는 키에 대해 디폴트를 리턴해주는 풀이 이용함
# 즉 키의 존재 여부 판별할 필요 없이 바로 계산 가능하다.

def numJewelsInStone2(J, S):
    freqs = collections.defaultdict(int)
    count = 0
    
    # 비교 없이 돌S의 빈도 수 계산
    for char in S:
        freqs[char] += 1

    # 비교 없이 보석J의 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count

print(numJewelsInStone2(J, S))

# 풀이 3 Counter로 계산 생략
# 각 개수를 계산하는 부분까지 자동으로 처리
# 특히 존재하지 않는 키의 경우 keyerror가 아닌 0을 출력해주므로, 예외 처리 할 필요 없음

def numJewelsInStone3(J, S):
    freqs = collections.Counter(S) # 돌S의 빈도 수 계산
    count = 0
    
    # 비교 없이 보석J의 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count

print(numJewelsInStone3(J, S))

# 풀이 4 파이썬다운 방식

def numJewelsInStone4(J, S):
    return sum(s in J for s in S)

print([s for s in S])
print([s in J for s in S])
print(sum(s in J for s in S))