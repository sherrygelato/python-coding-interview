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

# 다시 해볼 것@@@@@

# 문제 50 정렬된 배열의 이진 탐색 트리 변환 : 오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.

# 입력 
root = [-10, -3, 0, 5, 9]
# 출력 [0, -3, 9, -10, None, 5]

# 풀이 1 : 이진 검색 결과로 트리 구성

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


def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2 # 중앙값
    
    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid]) 
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])
    
    return node


print(sortedArrayToBST(root))