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
    # 문제 10 배열 파티션 1 : n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

    # 예제
    nums = [1, 4, 3, 2]
    # 4

    # 풀이 1 오름차순 풀이
    def arrayPairSum1(nums):
        # 페어의 min()을 합산했을 때 최대를 만드는 것은 결국 min()이 되도록 커야 하며, 
        # 뒤에서부터 내림차순으로 집어넣으면 항상 최대 min()을 유지할 수 있다.
        # 이 문제에서 배열 입력값은 항상 2n개일 것이라 앞에서부터 오름차순으로 넣어도 결과는 같을 것
        # 따라서 정렬된 상태에서 앞에서부터 오름차순으로 인접 요소 페어를 만들면 최대의 합이 된다.

        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    # 결과
    print(arrayPairSum1(nums))

    # 풀이 2 짝수 번째 값 계산
    def arrayPairSum2(nums):
        # 정렬된 상태에서는 짝수 번째 값(0부터 시작)에 항상 작은 값이 위치하기 때문에, 짝수 번째 값을 더하면 됨
        # 불필요한 리스트 변수 생략되어 간결하게 구현된다.

        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n
        
        return sum

    # 결과
    print(arrayPairSum2(nums))

    # 풀이 3 파이썬 다운 방식
    def arrayPairSum3(nums):
        # 슬라이싱 활용
        # 짝수 번째를 계산하는 것과 동일하면서도 해당 인덱스를 찾기만 하면 된다
        return sum(sorted(nums[::2]))

    # 결과
    print(arrayPairSum3(nums))
