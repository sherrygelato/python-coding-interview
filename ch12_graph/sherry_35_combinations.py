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

# 문제 35 조합 : 전체 수 n을 입력받아 k개의 조합을 리턴하라

# 예제 
n=4 
k=2
# 출력 [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]

# 풀이 1 DFS로 k개 조합 생성

def combine1(n, k):
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

print(combine1(n, k))

# 풀이 2 itertools 모듈 사용

def combine2(n, k):
    return list(itertools.combinations(range(1, n + 1), k))

print(combine2(n, k))