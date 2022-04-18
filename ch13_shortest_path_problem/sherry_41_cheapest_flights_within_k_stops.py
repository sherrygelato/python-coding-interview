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

# 문제 41 K 경유지 내 가장 저렴한 항공권 : 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라. 경로가 존재하지 않을 경우 -1을 리턴하라.
# 입력
n = 3
flights = [[0, 1, 100], [1,2,100], [0,2,500]]
src = 0
dst = 2
K = 0
# 출력 500

# 풀이 1 다익스트라 알고리즘 응용

def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1

print(findCheapestPrice(n, flights, src, dst, K))