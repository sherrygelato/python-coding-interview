"""
CH14. 46_Merge_Two_Binary_Trees.py
"""
import collections
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
lst1 = [1, 3, 2, 5, None, None, None]
input1 = toTree(lst1)
lst2 = [2, 1, 3, None, 4, None, 7]
input2 = toTree(lst2)
# 출력
output = [3, 4, 5, 5, 4, None, 7]

# --------------------------------------------------
def mergeTrees(t1, t2):
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = mergeTrees(t1.left, t2.left)
        node.right = mergeTrees(t1.right, t2.right)
        
        return node
    else:
        return t1 or t2


printTree(mergeTrees(input1, input2))
