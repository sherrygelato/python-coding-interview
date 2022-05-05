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

# 문제 46 두 이진 트리 병합 : 두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다.
# 입력
t1 = [1, 3, 2, 5, None, None, None]
t2 = [2, 1, 3, None, 4, None, 7]
# 출력 [3, 4, 5, 5, 4, None, 7]

# 풀이 1 재귀 탐색

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


t1 = toTree(t1)
t2 = toTree(t2)


def mergeTrees(t1, t2):
    if t1 and t2:
        node = TreeNode(t1.val+t2.val)
        node.left = mergeTrees(t1.left, t2.left)
        node.right = mergeTrees(t1.right, t2.right)

        return node
    # 어느 한쪽에 노드가 존재하지 않는다면
    else:
        # 존재하는 노드만 리턴하고 재귀 호출은 정지
        # 모두 존재하지 않는다면 None 리턴
        return t1 or t2
    

print(mergeTrees(t1, t2))