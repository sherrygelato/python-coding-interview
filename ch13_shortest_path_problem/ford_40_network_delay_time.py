"""
CH13. 40_Network_Delay_Time.py
"""
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect

# 입력 1
times = [[2,1,1], [2,3,1], [3,4,1]]
N = 4
K = 2

# 출력 1
output = 2

# 입력 2
times2 = [
    [3,1,5], [3,2,2], [2,1,2], [3,4,1], [4,5,1],
    [5,6,1], [6,7,1], [7,8,1], [8,1,1]
]
N2 = 8
K2 = 3

# 출력 2
output2 = 5

# --------------------------------------------------
def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    
    for u, v, w in times:
        graph[u].append((v, w))
        
    Q = [(0, K)]
    
    dist = collections.defaultdict(int)
    
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w, in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
                
    if len(dist) == N:
        return max(dist.values())
    return -1


print(networkDelayTime(times, N, K))
print(networkDelayTime(times, N, K) == output)
print(networkDelayTime(times2, N2, K2))
print(networkDelayTime(times2, N2, K2) == output2)