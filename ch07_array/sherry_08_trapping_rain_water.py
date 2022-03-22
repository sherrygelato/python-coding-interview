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

# 꼭 다시 보고 이해하기!

class Solution:
    # 문제 08 빗물 트래핑 : 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

    # 예제
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # 6

    # 풀이 1 투 포인터를 최대로 이동
    def trap1(height):
        # 막대는 높고 낮음에 무관하게, 전체 부피에 영향을 끼치지 않으면서 그저 왼쪽과 오른쪽을 가르는 장벽 역할을 한다.
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], height[right_max])
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left] 
                # 최대 높이의 막대까지 각각 좌우 기둥 최대 높이가 현재 높이와의 차이만큼 물 높이 volume을 더해나간다.
                left += 1
            else:
                volume += right_max - height[right]
                # 최대 높이의 막대까지 각각 좌우 기둥 최대 높이가 현재 높이와의 차이만큼 물 높이 volume을 더해나간다.
                right -= 1
            # 낮은 쪽은 그만큼 채워지기 때문에, 좌우 어느 쪽이든 낮은 쪽은 높은 쪽을 향해서 포인터가 가운데로 이동한다.
            # 오른쪽이 크다면 left += 1로 왼쪽으로, 아니면 right -= 1로 오론쪽으로 이동한다. 
            # 이런 식으로 가장 높은 막대 즉 최대 지점에서 좌우 포인터가 서로 만나게 되는 풀이
        return volume

    # 결과
    print(trap1(height))

    # 풀이 2 스택 쌓기
    def trap2(height):
        # 스택에 쌓아 나가면서 현재 높이가 이전 높이보다 높을 때, 꺽이는 부분 변곡점을 기준으로 격차만큼 물 높이 volume을 채운다.
        # 이전 높이는 고정된 형태가 아니기 때문에, 스택으로 채워 나가다가 변곡점을 만날 때마다 스택을 하나씩 꺼내 이전과의 차이만큼 물 높이를 채운다.
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break
                
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]] - height[top])

                volume += distance * waters

            stack.append(i)

        return volume

    # 결과
    print(trap2(height))
