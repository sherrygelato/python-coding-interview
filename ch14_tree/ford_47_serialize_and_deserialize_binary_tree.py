"""
CH14. 47_Serialize_and_Deserialize_Binary_Tree.py
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
lst = ['A', 'B', 'C', None, None, 'D', 'E']
# lst = [1, 2, 3, None, None, 4, 5]
input = toTree(lst)
# 출력

# --------------------------------------------------
def serialize(root):
    queue = collections.deque([root])
    result = ['#']
    
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            
            result.append(str(node.val))
        else:
            result.append('#')
    return ' '.join(result)

def deserialize(data):
    if data == '# #':
        return None
    
    nodes = data.split()
    
    root = TreeNode((nodes[1]))
    queue = collections.deque([root])
    index = 2
    
    while queue:
        node = queue.popleft()
        if nodes[index] != '#':
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1
        
        if nodes[index] != '#':
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
        
    return root


serialize(input)
printTree(deserialize(serialize(input)))