"""
CH09. 22_Daily_Temperatures.py
"""

# 입력
T = [73, 74, 75, 71, 69, 72, 76, 73]

# 출력: [1,1,4,2,1,1,0,0]

# --------------------------------------------------
def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        
        while stack and cur > T[stack[-1]]:
            print('  cur:', cur)
            print('  T[stack[-1]]', T[stack[-1]])
            last = stack.pop()
            answer[last] = i - last
            print(f'\nanswer[last] = {i} - {last}')
        stack.append(i)
        print('  Stack:', stack)
        print(f'-------------Cycle {i+1} done\n')
    
    return answer
        
        
print(dailyTemperatures(T))


# --------------------------------------------------