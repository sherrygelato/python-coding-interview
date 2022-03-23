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

# 문제 18 홀짝 연결 리스트 : 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.

# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next

# 예제 1 : 1 -> 2 -> 3 -> 4 -> 5 -> Null
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

l1 = node1  # 출력: 1 -> 3 -> 5 -> 2 -> 4 -> Null

# 예제 2 : 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7 -> Null
node12 = ListNode(7)
node11 = ListNode(4, node12)
node10 = ListNode(6, node11)
node9 = ListNode(5, node10)
node8 = ListNode(3, node9)
node7 = ListNode(1, node8)
node6 = ListNode(2, node7)

l2 = node6  # 출력: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4 -> Null

# 풀이 1 반복 구조로 홀짝 노드 처리
# 이 문제는 공간 복잡도와 시간 복잡도의 제약 사항이 있지만,
# 제약이 없을 경우, 연결 리스트를 리스트로 바꾸고 슬라이싱과 같은 함수를 사용하면 더 쉽고 직관적이게 풀이 가능하다.

# 홀수 노드 다음에 짝수 노드가 오게 재구성이니,
# 홀, 짝 각 노드를 구성한 다음,
# 홀수 노드의 마지막을 짝수 노드의 처음과 이어준다.

def oddEvenList(head):
    # 예외처리
    if head is None:
        return None
    
    # 첫번째 아이템
    odd = head # 홀수
    even = head.next # 짝수
    even_head = head.next # 짝수의 헤드

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        # 홀짝 처리를 하나로 묶어서 두줄로 처리하는 다중 할당으 ㄴ가능하다. 
        odd.next, even.next = odd.next.next, even.next.next 
        odd, even = odd.next, even.next 

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head

    return head

# 결과
printLinkedList(oddEvenList(l1))
print()
printLinkedList(oddEvenList(l2))
