"""
CH22. 84_Different_Ways_to_Add_Parentheses.py
"""

import collections
import enum
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력 1
input1 = "2-1-1"

# 출력 1
output1 = [2, 0]

# 입력 2
input2 = "2*3-4*5"

# 출력 2
output2 = [-34, -10, -14, -10, 10]


# --------------------------------------------------
def diffWaysToCompute(input):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results
    
    if input.isdigit():
        return [int(input)]
    
    results = []
    for index, value in enumerate(input):
        if value in "-+*":
            left = diffWaysToCompute(input[:index])
            right = diffWaysToCompute(input[index + 1:])
            
            results.extend(compute(left, right, value))
    return results


print(diffWaysToCompute(input1))
print(diffWaysToCompute(input1) == output1)
print(diffWaysToCompute(input2))
print(diffWaysToCompute(input2) == output2)
