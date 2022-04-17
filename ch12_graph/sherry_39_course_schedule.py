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

# 문제 39 코드 스케줄 : 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍으로 표현하는 n개의 코스가 있다. 코스 개수 n개의 코스가 있다. 코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.

# 예제 1
numCourses1 = 2
prerequisites1 = [[1,0]]
# 출력 true

# 예제 2
numCourses2 = 2
prerequisites2 = [[1,0], [0,1]]
# 출력 false

# 풀이 1 트리의 모든 DFS 결과

def canFinish1(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True

print(canFinish1(numCourses1, prerequisites1))
print(canFinish1(numCourses2, prerequisites2))

# 풀이 2 가지치기를 이용한 최적화

def canFinish2(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set() # 이미 한번 방문했던 노드

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 방문했던 노드이면 True : 가지치기로 탐색시간 줄이기
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True

print(canFinish2(numCourses1, prerequisites1))
print(canFinish2(numCourses2, prerequisites2))