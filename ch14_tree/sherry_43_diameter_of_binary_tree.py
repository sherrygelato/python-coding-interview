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

# 다시 할 것@@@@@@@@

# 문제 43 이진 트리의 직경 : 이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.
# 입력
root = [1,2,3,4,5,None,None]
# 출력 3

# 풀이 1 상태값 누적 트리 DFS
# 리프 노드까지 탐색한 다음 부모로 거슬러 올라가면서 각각의 거리를 계산해 상태값을 업데이트하면서 누적해 나간다.

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


root = toTree(root)
longest = [0]

def diameterOfBinaryTree(root):
    def dfs(node):
        # 존재하지 않는 노드에 -1라는 값 부여 (패널티 적용)
        if not node:
            return -1
        # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
        left = dfs(node.left)
        right = dfs(node.right)

        # 가장 긴 경로
        longest[0] = max(longest[0], left+right+2)
        # 상태값 : 리프 노드에서 현재 노드까지의 거리
        return max(left, right)+1

    dfs(root)
    return longest[0]
