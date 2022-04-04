"""
CH12. 39_Course_schedule.py
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
numCourses = 2
prerequisites = [[1,0]]

# 출력 1
output = True

# 입력 2
numCourses2 = 2
prerequisites2 = [[1,0], [0,1]]

# 출력 2
output2 = False

# --------------------------------------------------
def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()
    
    def dfs(i):
        if i in traced:
            return False
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        
        traced.remove(i)
        
        return True
    
    for x in list(graph):
        if not dfs(x):
            return False
        
    return True


print(canFinish(numCourses, prerequisites))

print(canFinish(numCourses2, prerequisites2))


# --------------------------------------------------
def canFinish2(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    
    for x, y in prerequisites:
        graph[x].append(y)
        
    traced = set()
    visited = set()
    
    def dfs(i):
        if i in traced:
            return False
        if i in visited:
            return True
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        
        traced.remove(i)
        visited.add(i)
        
        return True
    
    for x in list(graph):
        if not dfs(x):
            return False
    
    return True


print(canFinish2(numCourses, prerequisites))

print(canFinish2(numCourses2, prerequisites2))