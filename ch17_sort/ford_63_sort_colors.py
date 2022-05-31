"""
CH17. 63_Sort_Colors.py
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
input = [2,0,2,1,1,0]

# 출력
output = [0,0,1,1,2,2]


# --------------------------------------------------
def sortColors(nums):
    red, white, blue = 0, 0, len(nums)
    
    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1
    return nums


print(sortColors(input))
print(sortColors(input) == output)
