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

# 문제 40 네트워크 딜레이 타임 : K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 입력값(u, v, w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 갯수는 N으로 입력받는다.

# 입력
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
# 출력 2

# 풀이 1 다익스트라 알고리즘 구현 
# 판별해야할 사항 : 
# 1) 모든 노드가 신호를 받는데 걸리는 시간 - 가장 오래 걸리는 노드까지의 최단 시간
# 2) 모든 노드에 도달할 수 있는지 여부 - 모든 노드의 다익스트라 알고리즘 계산 값이 존재하는지 유무 판별. 하나라도 없으면 -1 리턴

def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    # 모든 노드 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1

print(networkDelayTime(times, N, K))