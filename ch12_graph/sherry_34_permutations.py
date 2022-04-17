#!/usr/bin/python3
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

# 문제 34 순열 : 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.

# 예제
input = [1,2,3] # 출력: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

# 풀이 1 DFS를 활용한 순열 생성
# 순열이란 결국 모든 가능한 경우를 그래프 형태로 나열한 결과

def permute1(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일때 결과 추가
        if len(elements) == 0:
            results.append(prev_elements[:])
            # 파이썬은 모든 객체를 참조하는 형태로 처리되므로, [:]나 copy(), deepcopy()로 처리한다.

        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

print(permute1(input))

# 풀이 2 itertools 모듈 사용
# itertools 모듈 : 반복자 생성에 최적화된 효율적인 기능 제공, 버그 발생 가능성이 낮고, 속도도 좋다.

def permute2(nums):
    return list(itertools.permutations(nums))

print(permute2(input))