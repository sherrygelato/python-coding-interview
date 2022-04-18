"""
CH14. 43_Diameter of Binary Tree.py
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
        if i > size or list[i-1] == None:
            return None
        node = TreeNode(list[i-1])
        node.left = recursive(2*i)
        node.right = recursive(2*i+1)
    
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
lst = [1,2,3,4,5,None,None]
input = toTree(lst)
input
# 출력
output = 3

# --------------------------------------------------
def diameterOfBinaryTree(root):
    longest = [0]
    def dfs(node):
        if not node:
            return -1
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        longest[0] = max(longest[0], left + right + 2)
        
        return max(left, right) + 1
    
    dfs(root)
    return longest[0]


print(diameterOfBinaryTree(input))
print(diameterOfBinaryTree(input) == output)
