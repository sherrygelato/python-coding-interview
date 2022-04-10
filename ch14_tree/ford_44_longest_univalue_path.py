"""
CH14. 44_Longest_Univalue_Path.py
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
lst1 = [5, 4, 5, 1, 1, None, 5]
input1 = toTree(lst1)
# 출력 1
output1 = 2

# 입력 2
lst2 = [1, 4, 5, 4, 4, None, 5]
input2 = toTree(lst2)
# 출력 2
output2 = 2

# --------------------------------------------------
def longestUnivaluePath(root):
    result = [0]
    
    def dfs(node):
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0
        
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0
        
        result[0] = max(result[0], left + right)
        return max(left, right)
    
    dfs(root)
    return result[0]


print(longestUnivaluePath(input1))
print(longestUnivaluePath(input1) == output1)

print(longestUnivaluePath(input2))
print(longestUnivaluePath(input2) == output2)