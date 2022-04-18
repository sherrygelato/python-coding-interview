"""
CH14. 49_Minimum_Height_Trees.py
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
n1 = 4
edges1 = [[1, 0], [1, 2], [1, 3]]
# 출력 1
output1 = [1]

# 입력 2
n2 = 6
edges2 = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 출력 2
output2 = [3, 4]

# 입력 3
n3 = 9
edges3 = [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]
# 출력 3
output3 = [3]

# --------------------------------------------------
def findMinHeightTrees(n, edges):
    if n <= 1:
        return [0]
    
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
        
    leaves = []
    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)
            
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
                
        leaves = new_leaves
        
    return leaves


print(findMinHeightTrees(n1, edges1))
print(findMinHeightTrees(n1, edges1) == output1)
print(findMinHeightTrees(n2, edges2))
print(findMinHeightTrees(n2, edges2) == output2)
print(findMinHeightTrees(n3, edges3))
print(findMinHeightTrees(n3, edges3) == output3)


# --------------------------------------------------
