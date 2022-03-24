"""
CH09. 20_ValidParentheses.py
"""

# 입력
s = '()[]{}'

# 출력: true

# --------------------------------------------------
def isValid(s):
    stack = []
    table = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


print(isValid(s))