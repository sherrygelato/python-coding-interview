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

# 문제 44 가장 긴 동일 값의 경로 : 동일한 값을 지닌 가장 긴 경로를 찾아라.
# 첫 번째 입력값을 기준으로 트리를 나타내고, 루트 노드부터 우측 리프 노드까지 이동 거리를 구하는 과정을 거치는데,
# 이 경우 루트 노드부터 DFS로 재귀 탐색을 진행하면서 리프에 도달하면 그때부터 백트래킹하면서 거리를 누적한다.

# 입력
root1 = [5, 4, 5, 1, 1, None, 5] # 출력 2
root2 = [1, 4, 5, 4, 4, None, 5] # 출력 2

# 풀이 1 상태값 거리 계산 DFS

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def toTree(list):
    size = len(list)
    idx = 1
    
    if size == 0:
        return None
    
    def recursive(i):
        if i > size or list[i-1] is None:
            return None
        node = TreeNode(list[i-1])
        node.left = recursive(2*i)
        node.right = recursive(2*i+1)
        
        return node
    return recursive(idx)


root1 = toTree(root1)
root2 = toTree(root2)

def longestUnivaluePath(root):
    
    result = [0]
    
    def dfs(node):
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0
        
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0
        
        result[0] = max(result[0], left + right)
        return max(left, right)
    
    dfs(root)
    return result[0]

print(longestUnivaluePath(root1))
print(longestUnivaluePath(root2))