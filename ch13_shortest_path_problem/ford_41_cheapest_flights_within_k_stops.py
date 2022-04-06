"""
CH13. 41_Cheapest_Flights_Within_K_Stops.py
"""
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect

# 입력
n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 0

# 출력
output = 500

# --------------------------------------------------
def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    
    for u, v, w in flights:
        graph[u].append((v, w))
        
    Q = [(0, src, K)]
    
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k-1))
    return -1


print(findCheapestPrice(n, edges, src, dst, K))
print(findCheapestPrice(n, edges, src, dst, K) == output)
