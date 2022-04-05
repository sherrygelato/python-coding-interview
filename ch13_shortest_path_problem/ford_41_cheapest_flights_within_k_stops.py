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
k = 0

# 출력
output = 500

# --------------------------------------------------
