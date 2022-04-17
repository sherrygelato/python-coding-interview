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

# 문제 38 일정 재구성 : [from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 잇는 경우 사전 어휘 순 Lexical Order으로 방문한다. 

# 예제 1
tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 출력 ["JFK", "MUC", "LHR", "SFO", "SJC"]

# 예제 2
tickets2 = [["JFK", "SFO"], ["JFK", "ALT"], ["SFO", "ALT"], ["ALT", "JFK"], ["ALT", "SFO"]]
# 출력 ["JFK", "ATL", "JFK", "SFO", "ALT", "SFO"]

# 풀이 1 DFS로 일정 그래프 구성

def findItinerary1(tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘순 방문
        while graph[a]:
            dfs(graph[a].pop(0)) # 큐의 연산 수행
        route.append(a)

    dfs('JFK')
    # 다시 뒤집어 어휘순 결과로
    return route[::-1]

print(findItinerary1(tickets1))
print(findItinerary1(tickets2))

# 풀이 2 스택 연산으로 큐 연산 최적화 시도

def findItinerary2(tickets):
    graph = collections.defaultdict(list)
    # 그래프 뒤집어서 구성
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 마지막 값을 읽어 어휘순 방문
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    # 다시 뒤집어 어휘순 결과로
    return route[::-1]

print(findItinerary2(tickets1))
print(findItinerary2(tickets2))

# 풀이 3 일정 그래프 반복
# 대부분의 재귀 문제는 반복으로 치환할 수 있으며, 스택으로 풀이가 가능

def findItinerary3(tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    # 다시 뒤집어 어휘순 결과로
    return route[::-1]

print(findItinerary3(tickets1))
print(findItinerary3(tickets2))