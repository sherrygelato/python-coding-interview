"""
CH14. 42_Maximum_Depth_of_Binary_Tree.py
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
        
def toBinaryTree(list):
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
input = [3, 9, 20, None, None, 15, 7]

# 출력
output = 3

tree = toBinaryTree(input)
printTree(tree)

# --------------------------------------------------
def maxDepth(root):
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0
    
    while queue:
        depth += 1
        
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    return depth


print(maxDepth(tree))
print(maxDepth(tree) == output)