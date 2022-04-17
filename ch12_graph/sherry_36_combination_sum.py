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

# 문제 36 조합의 합: 숫자 집합 andidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.

# 예제 1
candidates1 = [2,3,6,7]
target1 = 7
# 출력 : [[7], [2,2,3]]

# 예제 2
candidates2 = [2,3,5]
target2 = 8
# 출력 [[2,2,2,2], [2,3,3], [3,5]]

# 풀이 1 DFS로 중복 조합 그래프 탐색
# 합 target을 만들 수 있는 모든 번호 조합을 찾는 문제로
# 순열 문제와 유사하게 DFS깊이 우선 탐색과 백트래킹으로 풀이

def combinationSum(candidates, target):
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        # 자기 자신을 포함하기 때문에 무한히 탐색한다.
        if csum < 0: # 마이너스의 경우
            return
        if csum == 0: # 0인 경우
            result.append(path)
            return

        # 자신 부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result

print(combinationSum(candidates1, target1))
print(combinationSum(candidates2, target2))