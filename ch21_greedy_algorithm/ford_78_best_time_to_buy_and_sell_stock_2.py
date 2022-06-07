"""
CH21. 78_Best_Time_to_Buy_and_Sell_Stock_II.py
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


# 입력
input = [7, 1, 5, 3, 6, 4]

# 출력
output = 7


# --------------------------------------------------
def maxProfit(prices):
    result = 0
    
    for i in range(len(prices) -1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]
    return result


print(maxProfit(input))
print(maxProfit(input) == output)


# --------------------------------------------------
def maxProfit2(prices):
    return sum(max((prices[i+1]-prices[i]), 0) for i in range(len(prices) - 1))


print(maxProfit2(input))
print(maxProfit2(input) == output)
