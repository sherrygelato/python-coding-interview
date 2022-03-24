"""
CH09. 21_Remove_Duplicate_Letters.py
"""

# 입력 1
strA = 'bcabc'

# 출력 1: abc

# 입력 2
strB = 'cbacdcbc'

# 출력 2: acdb

# --------------------------------------------------
def removeDuplicateLetters(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


print(removeDuplicateLetters(strA))
print(removeDuplicateLetters(strB))


# --------------------------------------------------
import collections


def removeDuplicateLetters2(s):
    counter, seen, stack = collections.Counter(s), set(), []
    
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
        
    return ''.join(stack)


print(removeDuplicateLetters2(strA))
print(removeDuplicateLetters2(strB))


# --------------------------------------------------