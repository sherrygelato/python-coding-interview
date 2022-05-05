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

# 문제 47 이진 트리 직렬화 & 역직렬화 : 이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라. 즉 다음과 같은 트리는 [1,2,3,null, null, 4,5] 형태로 직렬화할 수 있을 것이다.

# 입력
root = [1, 2, 3, None, None, 4, 5]
# 출력 

# 풀이 1 직렬화 & 역직렬화 구현

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
        node.left = recursive(i*2)
        node.right = recursive(i*2+1)
        return node
    return recursive(idx)


# 직렬화
def serialize(root):
    queue = collections.deque([root])
    result = ['#']
    
    # 트리의 BFS 직렬화
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            
            result.append(str(node.val))
        else:
            result.append('#')
    return ' '.join(result)

# 역직렬화
def deserialize(data):
    # 예외처리
    if data == '# #':
        return None
    
    nodes = data.split()
    
    root = TreeNode((nodes[1]))
    queue = collections.deque([root])
    index = 2
    
    # 빠른 런너처럼 자식 노드 결과를 먼저 확인한 후 큐 삽입?
    while queue:
        node = queue.popleft()
        if nodes[index] != '#':
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1
        
        if nodes[index] != '#':
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
        
    return root


serialize(input)