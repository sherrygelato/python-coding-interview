"""
CH18. 69_Search_a_2D_Matrix_II.py
"""

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력
input = [
    [ 1,  4,  7, 11,  5],
    [ 2,  5,  8, 12, 19],
    [ 3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
         ]

target1 = 5
target2 = 20

# 출력
output1 = True
output2 = False


# --------------------------------------------------
def searchMatrix(matrix, target):
    if not matrix:
        return False
    
    row = 0
    col = len(matrix[0]) - 1
    
    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
    return False


print(searchMatrix(input, target1))
print(searchMatrix(input, target1) == output1)
print(searchMatrix(input, target2))
print(searchMatrix(input, target2) == output2)


# --------------------------------------------------
def searchMatrix2(matrix, target):
    return any(target in row for row in matrix)


print(searchMatrix2(input, target1))
print(searchMatrix2(input, target1) == output1)
print(searchMatrix2(input, target2))
print(searchMatrix2(input, target2) == output2)