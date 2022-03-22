#!/usr/bin/python3
"""
CH07. 10_Array_partition_1.py
"""

# 입력
nums = [1,4,3,2]

# 출력 = 4

# --------------------------------------------------
def arrayPairSum(nums):
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    
    return sum


print(arrayPairSum(nums))


# --------------------------------------------------
def arrayPairSum(nums):
    sum = 0
    nums.sort()
    
    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    
    return sum


print(arrayPairSum(nums))


# --------------------------------------------------
def arrayPairSum(nums):
    return sum(sorted(nums)[::2])


print(arrayPairSum(nums))


# --------------------------------------------------