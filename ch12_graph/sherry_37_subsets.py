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

# 문제 37 부분 집합 : 모든 부분 집합을 리턴하라

# 예제 
nums = [1,2,3]
# 출력 [[3], [1], [2], [1,2,3], [1,3], [1,2], [2,3], [1,2], []]

# 풀이 1 트리의 모든 DFS 결과

def subsets(nums):
    result = []

    def dfs(index, path):
        # 모든 탐색의 경로가 결국 정답이 됨, 매번 결과 추가
        result.append(path)

        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result

print(subsets(nums))