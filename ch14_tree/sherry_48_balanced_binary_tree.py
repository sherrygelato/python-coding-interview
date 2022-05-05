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

# 문제 48 균형 이진 트리 : 이진 트리가 높이 균형인지 판단하라. (높이 균형은 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것을 말한다.)

# 입력
root1 = [3, 9, 20, None, None, 15, 7]
root2 = [1, 2, 2, 3, 3, None, None, 4, 4]
# 출력 true, false

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


root1 = toTree(root1)
root2 = toTree(root2)


# 풀이 1 : 재귀 구조로 높이 차이 계산

# 균형이 맞아야 효율적으로 트리를 구성할 수 있으며, 탐색 또한 훨씬 더 효율적으로 처리할 수 있다.

def isBalanced(root):
    def check(root):
        if not root:
            return 0
        
        left = check(root.left)
        right = check(root.right)
        
        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return check(root) != -1


print(isBalanced(root1))
print(isBalanced(root2))