#!/usr/bin/python3
"""
CH07. 11_Product_of_Array_Except_Self.py
"""

# 입력
nums = [1,2,3,4]

# 출력 = [24, 12, 8, 6]

# --------------------------------------------------

def productExceptSelf(nums):
    out = []
    p = 1
    
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out


print(productExceptSelf(nums))


# --------------------------------------------------