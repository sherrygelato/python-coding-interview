#!/usr/bin/python3
"""
CH07. 12_Best_Time_to_Buy_and_Sell_Stock.py
"""

# 입력
prices = [7,1,5,3,6,4]

# 출력 = 5

# --------------------------------------------------
def maxProfit(prices):
    max_price = 0
    
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
            
    return max_price


print(maxProfit(prices))


# --------------------------------------------------
import sys


def maxProfit2(prices):
    profit = 0
    min_price = sys.maxsize
    
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit        

print(maxProfit2(prices))


# --------------------------------------------------
import sys


def maxProfit3(prices):
    profit = -sys.maxsize
    min_price = sys.maxsize
    
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit        

print(maxProfit3(prices))
