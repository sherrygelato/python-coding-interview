"""
CH14. 50_Convert_Sorted_Array_to_Binary_Search_Tree.py
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
input = [-10, -3, 0, 5, 9]
# 출력 
output = [0, -3, 9, -10, None, 5]

# 입력 2 
input2 = [-10, -7, -3, 0, 5, 7, 9]
# 출력 2
output2 = [0, -7, 7,-10, -3, 5, 9]

# --------------------------------------------------
def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])
    
    return node


print(printTree(sortedArrayToBST(input)))
print(printTree(sortedArrayToBST(input2)))
