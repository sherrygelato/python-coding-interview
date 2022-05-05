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

# 문제 49 최소 높이 트리 : 노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라.

# 입력
n1 = 4
edges1 = [[1, 0], [1, 2], [1, 3]] 
# 출력 [1]

n2 = 6
edges2 = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]] 
# 출력 [3, 4]

# 풀이 1 : 단계별 리프 노드 제거

# 그래프는 무방향이므로, 트리의 부모와 자식은 양쪽 노드 모두 번갈아 가능하다. 
# 따라서 양쪽 모두 그래프 딕셔너리 변수에 양방향으로 삽입해 구성한다. 
# n은 전체 노드 개수이므로 리프 노드의 개수만큼 계속 빼나가면서 최종 2개 이하가 나올 때까지 반복한다. 그래프를 두개 만들었으므로 제거 또한 두번씩 한다.

def findMinHeightTrees(n, edges):
    if n <= 1:
        return [0]
    
    # 양방향 그래프 구성
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
        
    # 첫번째 리프 노드 추가
    leaves = []
    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)

    # 루프 노드만 남을 때까지 반복 제거(양방향이니까 2번) 
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
                
        leaves = new_leaves
        
    return leaves


print(findMinHeightTrees(n1, edges1))
print(findMinHeightTrees(n2, edges2))