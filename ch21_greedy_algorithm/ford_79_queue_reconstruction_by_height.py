"""
CH21. 79_Queue_Reconstruction_by_Height.py
"""

import collections
import enum
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력
input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

# 출력
output = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]


# --------------------------------------------------
def reconstructionQueue(people):
    heap = []
    
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
    
    result = []
    
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result


print(reconstructionQueue(input))
print(reconstructionQueue(input) == output)
