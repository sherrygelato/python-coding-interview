"""
CH21. 81_Gas_Station.py
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
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# 출력
output = 3


# --------------------------------------------------
def canCompleteCircuit(gas, cost):
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas) + start):
            index = i % len(gas)
            
            can_travel = True
            if gas[index] + fuel < cost[index]:
                can_travel = False
                break
            else:
                fuel += gas[index] - cost[index]
        if can_travel:
            return start
    return -1


print(canCompleteCircuit(gas, cost))
print(canCompleteCircuit(gas, cost) == output)


# --------------------------------------------------
def canCompleteCircuit2(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    start, fuel = 0, 0
    for i in range(len(gas)):
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start


print(canCompleteCircuit2(gas, cost))
print(canCompleteCircuit2(gas, cost) == output)
