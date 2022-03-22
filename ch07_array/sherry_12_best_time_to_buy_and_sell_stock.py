# -*- coding:UTF-8 -*-

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import Deque

class Solution:
    # 문제 12 주식을 사고팔기 가장 좋은 시점 : 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

    # 예제
    prices = [7, 1, 5, 3, 6, 4]
    # 5

    # 풀이 1 브루트 포스로 계산
    def maxProfit1(prices):
        # 저점에서 사서 고점에 팔아 낼 수 있는 최대 이익을 찾는 문제
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

    # 결과
    print(maxProfit1(prices))

    # 풀이 2 저점과 현재 값과의 차이 계산
    def maxProfit2(prices):
        # 그래프를 그려봤을 때, 현재값을 가리키는 포인터가 우측으로 이동하면서 이전 상태의 저점을 기준으로 가격 차이를 계산하고,
        # 만약 클 경우 최댓값을 계속 교체하는 형태로 가능할 듯
        # 이러한 시각화는 기술 통계학 Descriptive Statistics이다.

        # 최댓값, 최솟값 선언
        profit = -sys.maxsize
        min_price = sys.maxsize
        # 각각 시스템의 가장 작은 값, 가장 큰 값으로 정한다.
        # 최댓값 변수는 최솟값으로, 최솟값 변수는 최댓값으로 지정해야 어떤 값이 들어오든 바로 교체될 수 있다. (none일 시 TypeError 발생)
        # 단, 최대 이익 profit이 최종 결과로 리턴되는데 입력값이 []인 경우, 즉 빈 배열일 경우 -sys.maxsize가 그대로 리턴될 수 있다.
        
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

    # 결과
    print(maxProfit2(prices))
