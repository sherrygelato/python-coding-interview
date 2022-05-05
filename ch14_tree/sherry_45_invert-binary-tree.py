# Python
# -*- coding:UTF-8 -*-

import collections
import heapq
import functools
import itertools
import queue
import re
import sys
import math
import bisect
# from typing import *

# 문제 45 이진 트리 반전 : 좌우 반전

# 입력
root = [4, 2, 7, 1, 3, 6, 9] 
# 출력 [4, 7, 2, 9, 6, 3, 1] 

# 풀이 1 파이썬다운 방식

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


def invertTree1(root):
    if root:
        root.left, root.right = \
            invertTree1(root.right), invertTree1(root.left)
        return root
    return None
    
print(invertTree1(root))

# 풀이 2 반복 구조로 BFS

def invertTree2(root):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft() # 처음값 추출
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            # 스왑하면서 큐에 추가
            queue.append(node.left)
            queue.append(node.right)
    
    return root

print(invertTree2(root))

# 풀이 3 반복 구조로 DFS

def invertTree3(root):
    stack = collections.deque([root])

    while stack:
        node = stack.pop() # 마지막 값 추출
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            stack.append(node.left)
            stack.append(node.right)
    
    return root

print(invertTree3(root))

# 풀이 4 반복 구조로 DFS 후위 순회

def invertTree4(root):
    stack = collections.deque([root])

    while stack:
        node = stack.pop() # 마지막 값 추출

        if node:
            stack.append(node.left)
            stack.append(node.right)

            # 후휘 순회
            node.left, node.right = node.right, node.left
    
    return root

print(invertTree4(root))