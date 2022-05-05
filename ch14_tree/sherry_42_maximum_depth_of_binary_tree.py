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

# 문제 42 이진 트리의 최대 깊이 : 이진 트리의 최대 깊이를 구하라.
# 입력
root = [3, 9, 20, None, None, 15, 7]
# 출력 3

# 풀이 1 반복 구조로 BFS(너비 우선 탐색) 풀이
# 재귀가 아닌 반복 구조로 풀이 가능하다.
# DFS는 스택, BFS는 큐를 사용하여 구현한다.
# 파이썬에서의 큐는 일반적인 리스트로도 모든 연산이 가능하지만, 
# 데크 자료형을 사용하면 이중 연결 리스트로 구성되어 있어, 
# 큐와 스택 연산을 모두 자유롭게 활용 가능할 뿐만 아니라 양방향 모두 O(1)에 추출할 수 있어 좋은 성능을 보인다.

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


def maxDepth(root):
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0

    # 큐를 선언하고 반복 구조도 구성하여 BFS 반복 이용해 풀이
    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft() # popleft() 하나씩 끄집어 낸다.
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    # BFS 반복 횟수 == 깊이
    return depth

print(maxDepth(root))