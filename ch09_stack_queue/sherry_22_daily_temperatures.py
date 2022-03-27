# Python
# -*- coding:UTF-8 -*-

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# 문제 22 일일 온도 : 매일의 화씨 온도 리스트 T를 입력 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

# 예제
T = [73, 74, 75, 71, 69, 72, 76, 73] # 출력 [1, 1, 4, 2, 1, 1, 0, 0]

# 풀이 1 스택 값 비교
 
def dailyTemperatures(T):
    # 현재의 인덱스를 계속 스택에 쌓아두다가, 
    # 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도 차이를 비교, 
    # 더 높다면 스택의 값을 꺼내고, 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 처리
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer

print(dailyTemperatures(T))