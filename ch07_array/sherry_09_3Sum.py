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
    # 문제 09 세 수의 합 : 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

    # 예제
    nums = [-1, 0, 1, 2, -1, -4]
    # [[-1, 0, 1], [-1, -1, 2]]

    # 풀이 1 브루트 포스로 계산
    def threeSum1(nums):
        result = []
        # 앞뒤로 같은 값이 있을 경우, 먼저 정렬한다.
        nums.sort()

        # 브루트 포스 n^3 반복 
        for i in range(len(nums) -2):
            # i, j, k 각각의 포인터가 계속 이동하면서 i+j+k=0을 찾아낸다.
            # 중복된 값이 있을 수 있으므로 continue로 건너뛰게 한다.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])

        return result

    # 결과
    print(threeSum1(nums))

    # 풀이 2 투 포인터로 합 계산
    def threeSum2(nums):
        result = []
        nums.sort()

        # i를 축으로 하고 중복된 값을 건너뛴다.
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #  간격을 좁혀가며 합 sum 계산
            # 중복이 아닌 경우 투 포인터로 풀이한다.
            # i의 다음 지점과 마지막 지점을 left, right로 설정하여 간격을 좁혀가며 sum을 계산한다.
            left, right = i+1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                # 투 포인터가 간격을 좁혀나가면서 합 sum을 계산한다.
                if sum < 0:
                    # sum < 0이면 값을 더 키워야 하므로 left를 우측으로
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0이면 정답 및 스킵 처리
                    result.append([nums[i], nums[left], nums[right]])
                
                # left, right 앙 옆으로 동일한 값이 있을 수 있으므로 반복해서 스킵 처리
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                # 나머지 값 찾으려면 둘 다 모두 움직여야 한다.
                left += 1
                right -= 1
        
        return result

    # 결과
    print(threeSum2(nums))
