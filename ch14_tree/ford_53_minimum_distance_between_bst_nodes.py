"""
CH14. 53_Minimum_Distance_Between_BST_Nodes.py
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
root1 = [4, 2, 6, 1, 3, None, None]
input1 = toTree(root1)
# 출력 1 
output1 = 1

# 입력 2
root2 = [10, 4, 15, 1, 8, None, None]
input2 = toTree(root2)
# 출력 2
output2 = 2

# 입력 3
root3 = [8, 4, 12, 2, 6, None, None, 1, 3, 5, 7]
input3 = toTree(root3)
# 출력 3
output3 = 1

# --------------------------------------------------
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result

sol = Solution()
print(sol.minDiffInBST(input1))
sol = Solution()
print(sol.minDiffInBST(input1) == output1)
sol = Solution()
print(sol.minDiffInBST(input2))
sol = Solution()
print(sol.minDiffInBST(input2) == output2)
sol = Solution()
print(sol.minDiffInBST(input3))
sol = Solution()
print(sol.minDiffInBST(input3) == output3)


# --------------------------------------------------
def minDiffInBST2(root):
    prev = -sys.maxsize
    result = sys.maxsize
    
    stack = []
    node = root
    
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        
        result = min(result, node.val - prev)
        prev = node.val
        
        node = node.right
    
    return result


print(minDiffInBST2(input1))
print(minDiffInBST2(input1) == output1)
print(minDiffInBST2(input2))
print(minDiffInBST2(input2) == output2)
print(minDiffInBST2(input3))
print(minDiffInBST2(input3) == output3)
