"""
CH17. 64_K_Closest_Points_to_Origin.py
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
points1 = [[1, 3], [-2, 2]]
k1 = 1

# 출력 1
output1 = [[-2, 2]]

# 입력 2
points2 = [[3, 3], [5, -1], [-2, 4]]
k2 = 2

# 출력 2
output2 = [[3, 3], [-2, 4]]


# --------------------------------------------------
def kClosest(points, k):
    heap = []
    for (x, y) in points:
        dist = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
        heapq.heappush(heap, (dist, x, y))
    
    result = []
    for _ in range(k):
        dist, x, y = heapq.heappop(heap)
        result.append([x, y])
    return result


print(kClosest(points1, k1))
print(kClosest(points1, k1) == output1)
print(kClosest(points2, k2))
print(kClosest(points2, k2) == output2)


# --------------------------------------------------
def kClosest2(points, k):
    heap = []
    for (x, y) in points:
        dist = x ** 2 + y ** 2
        heapq.heappush(heap, (dist, x, y))
    
    result = []
    for _ in range(k):
        dist, x, y = heapq.heappop(heap)
        result.append([x, y])
    return result


print(kClosest2(points1, k1))
print(kClosest2(points1, k1) == output1)
print(kClosest2(points2, k2))
print(kClosest2(points2, k2) == output2)


# --------------------------------------------------
