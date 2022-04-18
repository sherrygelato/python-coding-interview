"""
CH14. 48_Balanced_Binary_Tree.py
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


# 입력 1
lst1 = [3, 9, 20, None, None, 15, 7]
input1 = toTree(lst1)
# 출력 1
output1 = True

# 입력 2
lst2 = [1, 2, 2, 3, 3, None, None, 4, 4]
input2 = toTree(lst2)
# 출력 2
output2 = False

# --------------------------------------------------
def isBalanced(root):
    def check(root):
        if not root:
            return 0
        
        left = check(root.left)
        right = check(root.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return check(root) != -1


print(isBalanced(input1))
print(isBalanced(input1) == output1)
print(isBalanced(input2))
print(isBalanced(input2) == output2)


# --------------------------------------------------
