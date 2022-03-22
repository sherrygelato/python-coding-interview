#!/usr/bin/python3
"""
CH07. 08_Trapping_Rain_Water.py
"""

# 입력
height = [0,1,0,2,1,0,1,3,2,1,2,1]
'''
              o
      o # # # o o # o  
  o # o o # o o o o o o
* * * * * * * * * * * * 
'''

# 출력 = 6

# --------------------------------------------------
def trap(height):
    if not height:
        return 0
    
    volume = 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


print(trap(height))


# --------------------------------------------------
def trap(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        print(i+1, '회차')
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            print('  top:',top)
            print('  height[i]:',height[i])
            if not len(stack):
                break
            
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            
            volume += distance * waters
            print('  volume:',volume)
        else:
            print('-----while 패스-----')
        stack.append(i)
        print('  stack:',stack)
    return volume


print(trap(height))


# --------------------------------------------------