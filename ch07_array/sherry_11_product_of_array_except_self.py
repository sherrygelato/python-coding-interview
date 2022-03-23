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
from typing import Deque

# 문제 11 자신을 제외한 배열의 곱 : 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라. 주의: 나눗셈을 하지 않고 O(n)에 풀이하라.

# 예제
nums = [1, 2, 3, 4]
# [24, 12, 8, 6]

# 풀이 1 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def productExceptSelf(nums):
    # "나눗셈을 하지 않고 O(n)에 풀이하라." => 미리 전체 곱셈 값을 구해놓고 각 항목별로 자기 자신을 나눠서 풀이하는 방법은 안된다.
    # 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱해야 한다.
    out = []
    p = 1

    # 왼쪽 곱셈
    # 왼쪽부터 곱해서 결과는 out 리스트 변수에 담고, 마지막 값 곱셈을 제외
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    # print(out)
    
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) -1, 0 -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out

# 결과
print(productExceptSelf(nums))
