#!/usr/bin/python3
"""
CH06. 01_Valid_Palindrome
"""

strA = "A man, a plan, a canal: Panama"
strB = "race a car"
strC = "race a ecar"


# --------------------------------------------------
def isPalindromeWithList(s):
    """String -> List로 한 문자씩 비교"""
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


print(isPalindromeWithList(strA))  # True
print(isPalindromeWithList(strB))  # False
print(isPalindromeWithList(strC))  # True


# --------------------------------------------------
from collections import deque


def isPalindromeWithDeque2(s):
    """String -> deque로 한 문자열씩 비교"""
    strs: deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(isPalindromeWithDeque2(strA))  # True
print(isPalindromeWithDeque2(strB))  # False
print(isPalindromeWithDeque2(strC))  # True


# --------------------------------------------------
import re


def isPalindromeWithSlicing3(s):
    """전체 소문자로 변경/특수문자 제거 후 슬라이싱을 통한 비교"""
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


print(isPalindromeWithSlicing3(strA))  # True
print(isPalindromeWithSlicing3(strB))  # False
print(isPalindromeWithSlicing3(strC))  # True
