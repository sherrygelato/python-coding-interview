"""
CH14. 52_Range_Sum_of_BST.py
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
root = [10, 5, 15, 3, 7, None, 18]
L = 7
R = 15
input = toTree(root)
# 출력 
output = 32

# --------------------------------------------------
def rangeSumBST(root, L, R):
    if not root:
        return 0
    
    return (root.val if L <= root.val <= R else 0) + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R)


print(rangeSumBST(input, L, R))
print(rangeSumBST(input, L, R) == output)


# --------------------------------------------------
def rangeSumBST2(root, L, R):
    def dfs(node):
        if not node:
            return 0
        
        if node.val < L:
            return dfs(node.right)
        elif R < node.val:
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)
    
    return dfs(root)


print(rangeSumBST2(input, L, R))
print(rangeSumBST2(input, L, R) == output)


# --------------------------------------------------
def rangeSumBST3(root, R, L):
    stack, sum = [root], 0
    
    while stack:
        node = stack.pop()
        if node:
            if  L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    return sum

print(rangeSumBST3(input, R, L))
print(rangeSumBST3(input, R, L) == output)


# --------------------------------------------------
def rangeSumBST4(root, R, L):
    stack, sum = [root], 0
    
    while stack:
        node = stack.pop(0)
        if node:
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    return sum


print(rangeSumBST4(input, R, L))
print(rangeSumBST4(input, R, L) == output)