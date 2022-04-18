"""
CH14. 51_Binary_Search_Tree_to_Greater_Sum_Tree.py
"""
import collections
from gc import collect
import heapq
import functools
import itertools
import re
import sys
import math
import bisect

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


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


def printTree(root):
    if root is None:
        print('Tree is Empty')
        
    q = collections.deque([root])
    
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            print(cur.val, end = ' ')
        print()


# 입력 
input = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
# 출력 
output = [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]

# --------------------------------------------------
