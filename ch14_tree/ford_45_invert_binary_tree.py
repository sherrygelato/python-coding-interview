"""
CH14. 45_Invert_Binary_Tree.py
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
lst = [4, 2, 7, 1, 3, 6, 9]
input = toTree(lst)
# 출력
output = [4, 7, 2, 9, 6, 3, 1]

# --------------------------------------------------
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root


printTree(invertTree(input))
printTree(toTree(output))


# --------------------------------------------------
def invertTree2(root):
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            node.left, node.right = node.right, node.left
            
            queue.append(node.left)
            queue.append(node.right)
            
    return root


printTree(invertTree2(input))
printTree(toTree(output))


# --------------------------------------------------
def invertTree3(root):
    stack = collections.deque([root])
    
    while stack:
        node = stack.pop()
        
        if node:
            node.left, node.right = node.right, node.left
            
            stack.append(node.left)
            stack.append(node.right)
    
    return root


printTree(invertTree3(input))
printTree(toTree(output))


# --------------------------------------------------
def invertTree4(root):
    stack = collections.deque([root])
    
    while stack:
        node = stack.pop()
        
        if node:
            stack.append(node.left)
            stack.append(node.right)
            
            node.left, node.right = node.right, node.left
            
    return root


printTree(invertTree4(input))
printTree(toTree(output))