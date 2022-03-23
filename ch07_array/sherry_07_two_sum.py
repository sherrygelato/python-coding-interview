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

# 문제 07 두 수의 합 : 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# 예제
nums = [2, 7, 11, 15]
target = 9
# [0, 1]

# 풀이 1 브루트 포스로 계산
def twoSum1(nums, target):
    # 브루트 포스Brute-Force: 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식
    # - 단점 : 지나치게 느림
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
                
# 결과
print(twoSum1(nums, target))

# 풀이 2 in을 이용한 탐색
def twoSum2(nums, target):
    # 모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값 target-n이 존재하는지 탐색
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement)+(i+1)]

# 결과
print(twoSum2(nums, target))

# 풀이 3 첫 번째 수를 뺀 결과 키 조회
def twoSum3(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

# 결과
print(twoSum3(nums, target))

# 풀이 4 조회 구조 개선
def twoSum4(nums, target):
    # 저장 및 조회를 하나의 for로 합쳐서 처리
    # 전체 모두 저장할 필요 없이 정답을 찾게 되면 함수를 바로 빠져나옴
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# 결과
print(twoSum4(nums, target))

# 풀이 5 투 포인터 이용
def twoSum5(nums, target):
    # 투 포인터 : 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

# 결과
print(twoSum5(nums, target))
