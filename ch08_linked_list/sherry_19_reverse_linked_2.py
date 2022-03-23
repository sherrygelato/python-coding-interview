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

# 문제 19 역순 연결 리스트 2 : 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next

# 예제 1 : 1 -> 2 -> 3 -> 4 -> 5 -> Null, m = 2, n = 4
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head = node1  # 출력: 1 -> 4 -> 3 -> 2 -> 5 -> Null
m = 2
n = 4

# 풀이 1 반복 구조로 노드 뒤집기
def reverseBetween(head, m, n):
    # 예외처리
    if not head or m == n:
        return head
    
    root = start = ListNode(None) # start : 변경이 필요한 m의 바로 앞 지점인 m-1
    root.next = head # head 이전보다 root를 만들어서 최종결과로 root.next 리턴 
    # start, end 지점
    for _ in range(m-1):
        start = start.next 
    end = start.next

    # 반복하면서 노드 차례대로 뒤집기
    for _ in range(n-m):
        tmp, start.next, end.next = start.next, end.next, end.next.next 
        start.next.next = tmp 

    return root.next  

# 결과
printLinkedList(reverseBetween(head, m, n))
