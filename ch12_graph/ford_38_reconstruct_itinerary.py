"""
CH12. 38_Reconstruct_Itinerary.py
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
tickets = [
    ['MUC', 'LHR'],
    ['JFK', 'MUC'],
    ['SFO', 'SJC'],
    ['LHR', 'SFO']
]

# 출력 1
output = [
    'JFK',
    'MUC',
    'LHR',
    'SFO',
    'SJC'
    ]

# 입력 2
tickets2 = [
    ['JFK', 'SFO'],
    ['JFK', 'ATL'],
    ['SFO', 'ATL'],
    ['ATL', 'JFK'],
    ['ATL', 'SFO']
]

# 출력 2
output2 = [
    'JFK',
    'ATL',
    'JFK',
    'SFO',
    'ATL',
    'SFO'
    ]

# --------------------------------------------------
def findItinerary(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
        
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    
    dfs('JFK')
    return route[::-1]


print(findItinerary(tickets))
print(findItinerary(tickets) == output)

print(findItinerary(tickets2))
print(findItinerary(tickets2) == output2)


# --------------------------------------------------
def findItinerary2(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse = True):
        graph[a].append(b)
    
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)
    
    dfs('JFK')
    return route[::-1]


print(findItinerary2(tickets))
print(findItinerary2(tickets) == output)

print(findItinerary2(tickets2))
print(findItinerary2(tickets2) == output2)


# --------------------------------------------------
def findItinerary3(tickets):
    graph = collections.defaultdict(list)
    
    for a, b in sorted(tickets):
        graph[a].append(b)
        
    route, stack = [], ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    
    return route[::-1]


print(findItinerary3(tickets))
print(findItinerary3(tickets) == output)

print(findItinerary3(tickets2))
print(findItinerary3(tickets2) == output2)