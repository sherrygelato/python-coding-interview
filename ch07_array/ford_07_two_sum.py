#!/usr/bin/python3
"""
CH07. 07_Two_Sum.py
"""

# 입력
nums = [2,7,11,15]
target = 9
# 출력 = [0, 1]

# --------------------------------------------------
def twoSum(nums, target):
    """1. 브루트포스로 모든 경우의수 계산"""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum(nums, target))


# --------------------------------------------------
def twoSum2(nums, target):
    """2. in을 이용한 탐색"""
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]


print(twoSum2(nums, target))


# --------------------------------------------------
def twoSum3(nums, target):
    """3. target-num을 dictionary를 활용해 확인"""
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


print(twoSum3(nums, target))


# --------------------------------------------------
def twoSum4(nums, target):
    """4. 3을 좀 더 간단하게 축약, 성능상 개선은 미미함."""
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


print(twoSum4(nums, target))


# --------------------------------------------------
def twoSum5(nums, target):
    """이 문제는 nums가 정렬되었다는 보장이 없으므로, 투포인터로 풀 수 없음!"""
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


print(twoSum5(nums, target))
