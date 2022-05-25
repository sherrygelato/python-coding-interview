"""
CH14. 54_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.py
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


# 입력 1 
input11 = [3, 9, 20, 15, 7]
input12 = [9, 3, 15, 20, 7]
# 출력 1
root1 = [3, 9, 20, None, None, 15, 7]
input1 = toTree(root1)

# 입력 2
input21 = [1, 2, 4, 5, 3, 6, 7, 9, 8]
input22 = [4, 2, 5, 1, 7, 9, 6, 8, 3]
# 출력 2
root2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
input2 = toTree(root2)


# --------------------------------------------------
def buildTree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        
        node = TreeNode(inorder[index])
        node.left = buildTree(preorder, inorder[0: index])
        node.right = buildTree(preorder, inorder[index + 1:])
        
        return node
    
print(printTree(buildTree(input11, input12)))
print(printTree(buildTree(input21, input22)))