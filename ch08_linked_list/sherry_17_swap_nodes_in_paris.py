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

# 문제 17 페어의 노드 스왑 : 연결 리스트를 입력받아 페어 단위로 스왑하라

# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next

# 예제 1 : 1->2->3->4 
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head = node1  # 출력: 2->1->4->3

# 풀이 1 값만 교환
# 노드 구조는 그대로 유지하되 값만 변경하는 방법으로 풀이
def swapPairs1(head):
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next 
    
    return head

# 결과
printLinkedList(swapPairs1(head))

# 풀이 2 반복 구조로 스왑
def swapPairs2(head):
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next 
        head.next = b.next 
        b.next = head

        # 아직 a의 이전 노드가 b를 가리키지는 못하기 때문에,
        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next 
        prev = prev.next.next 

    return root.next 

# 결과
printLinkedList(swapPairs2(head))

# 풀이 3 재귀 구조로 스왑
def swapPairs3(head):

    if head and head.next:
        # 포인터 역할을 하는 p
        p = head.next 
        # 스왑된 값 리턴
        head.next = swapPairs3(p.next)
        p.next = head
        return p

    return head

# 결과
printLinkedList(swapPairs3(head))
