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

# 문제 13 팰린드롬 연결 리스트 : 연결 리스트가 팰린드롬 구조인지 판별하라.

# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 예제 1 : 1->2
node2 = ListNode(2)
node1 = ListNode(1, node2)

# 예제 2 : 1->2->2->1
node6 = ListNode(1)
node5 = ListNode(2, node6)
node4 = ListNode(2, node5)
node3 = ListNode(1, node4)

# 입력
head1 = node1  # false
head2 = node3  # true

# 풀이 1 리스트 변환

def isPalindrome1(head):
    # 앞뒤로 모두 추출할 수 있는 자료 구조 필요
    # 파이썬의 리스트는 pop() 함수에 (자유롭게) 인덱스 지정 가능
    # 연결 리스트를 파이썬의 리스트로 변환하여 리스트의 기능 이용하여 풀이

    q : List = []

    if not head:
        return True

    node = head 
    # 리스트로 변환
    while node is not None:
        q.append(node.val)
        node = node.next
        # print("1", q)

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            # print("2", q)
            return False

    return True

# 결과
print(isPalindrome1(head1))
print(isPalindrome1(head2))

# 풀이 2 데크를 이용한 최적화

def isPalindrome2(head):
    # 동적 배열로 구성된 리스트는 맨 앞 값을 가져오기에 적합한 자료형이 아니기 때문에,
    # q.pop(0)에서 첫번째 값을 추출할 때의 속도 문제가 존재함
    # 첫번째 값을 꺼내오면 모든 값이 한 칸씩 Shifting되며 시간 복잡도 O(n)이 발생하기 때문이다.

    # 이러한 문제를 해결하기 위해 맨 앞 데이터를 가져올 때 O(n) 이내 처리할 자료형이 필요
    # 즉, Deque

    # Deque는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 시간 복잡도 O(1)에 실행된다.
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
        # print("1", q)

    # 팰린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            # print("2", q)
            return False

    return True

# 결과
print(isPalindrome2(head1))
print(isPalindrome2(head2))

# 풀이 4 Runner를 이용한 우아한 풀이

def isPalindrome3(head):
    # 느린 러너가 중간까지 이동하면서 역순으로 연결 리스트 rev를 만듦
    rev = None
    # 빠른 러너와 느린 러너의 출발점은 head
    slow = fast = head

    # 러너의 이동 : next가 존재하지 않을 때까지
    while fast and fast.next:
        # fast 두칸씩
        fast = fast.next.next 
        # slow 한칸씩
        # rev 역순으로 연결 리스트 rev를 생성하는 로직
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 역순 연결 리스트를 반복해서 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev

print(isPalindrome3(head1))
print(isPalindrome3(head2))
