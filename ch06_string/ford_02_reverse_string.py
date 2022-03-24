#!/usr/bin/python3
"""
CH06. 02_Reverse_String
"""

strA = list("hello")
strB = list("hannah")


# --------------------------------------------------
def reverseStringWithTwoPointer(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

print(reverseStringWithTwoPointer(strA))  # ['o', 'l', 'l', 'e', 'h']
print(reverseStringWithTwoPointer(strB))  # ['h', 'a', 'n', 'n', 'a', 'h']


# --------------------------------------------------
def reverseStringWithPython2(s):
    s.reverse()

    return s


print(reverseStringWithPython2(strA))  # ['o', 'l', 'l', 'e', 'h']
print(reverseStringWithPython2(strB))  # ['h', 'a', 'n', 'n', 'a', 'h']
