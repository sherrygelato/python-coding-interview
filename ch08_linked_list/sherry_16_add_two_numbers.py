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
from typing import *

# TODO: 다시 보면서 이해하기!

# 문제 16 두 수의 덧셈 : 역순으로 저장된 연결 리스트의 숫자를 더하라.

# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next

# 예제 1 : (2 -> 4 -> 3) + (5 -> 6 -> 4)
node6 = ListNode(4)
node5 = ListNode(6, node6)
node4 = ListNode(5, node5)

node3 = ListNode(3)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)

l1 = node1
l2 = node4

# 입력 l1, l2를 하면 출력: 7 -> 8 -> 0

# 풀이 1 자료형 변환
# 연결 리스트를 문자열로 이어 붙인 다음 숫자로 변환, 이를 계산 후 다시 연결 리스트로 바꾸는 풀이

# 역순으로 된 연결 리스트를 뒤집기
def reverseList2(head):
    node, prev = head, None

    # node를 반복하여 값을 리스트에 추가
    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# 덧셈 연산 위해 연결 리스트를 파이썬 리스트로 변경
def toList(node):
    list = []

    while node:
        list.append(node.val)
        node = node.next 

    return list

# 리스트를 연결리스트로 변경
def toReversedLinkedList(result):
    prev = None

    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node

# 최종 풀이
def addTwoNumbers1(l1, l2):
    # 연결 리스트 뒤집고 리스트로 변환
    b = toList(reverseList2(l2))
    a = toList(reverseList2(l1))

    # str()으로 각 항목을 문자로 변경 후, ''.join()으로 문자열로 합침 
    resultStr = int(''.join(str(e) for e in a)) + \
        int(''.join(str(e) for e in b))

    # 최종 결과를 연결 리스트로 변경
    return toReversedLinkedList(str(resultStr))

# 결과
printLinkedList(addTwoNumbers1(l1, l2))

# 풀이 2 전가산기 구현 Full Adder
# 이진법이 아닌 십진법으로 자리올림수Carry를 구하는 것으로 논리 회로의 전가산기와 유사한 구현 풀이 
# 입력값 A, B, 이전의 자리 올림수 Carry in 3가지 입력으로 sum과 다음 자리수 Carry out여부를 결정
def addTwoNumbers2(l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum += l1.val
            l1 = l1.next 
        if l2:
            sum += l2.val
            l2 = l2.next 
        
        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10) 
            # 자리올림수 계산, divmod()는 몫과 나머지로 구성된 튜플 리턴
        head.next = ListNode(val)
        head = head.next 

    return root.next

# 결과
printLinkedList(addTwoNumbers2(l1, l2))
