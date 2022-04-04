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
# from typing import *

# 문제 28 해시맵 디자인 : 다음의 기능을 제공하는 해시맵을 디자인하라.
"""
- put(key, value) : 키, 값을 해시맵에 삽입, 만약 이미 존재한다면 업데이트
- get(key) : 키에 해당하는 값 조회, 만약 키 존재하지 않다면 -1 리턴
- remove(key) : 키에 해당하는 키, 값을 해시맵에서 삭제

hashMap = MyHashMap()
hashMap
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)
hashMap.get(2)
hashMap.put(2, 3)
hashMap.get(2)
hashMap.remove(2)
hashMap.get(2)
"""

# 풀이 1 개별 체이닝 방식을 이용한 해시 테이블 구현

class ListNode:
    # 키, 값을 보관하고 연결 리스트로 처리할 별도의 객체
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self, size = 1000):
        self.size = size
        self.table = collections.defaultdict(ListNode)
        # 존재하지 않는 키 조회 시 자동으로 디폴트를 생성해주는 defaultdict


    def put(self, key, value):
        index = key % self.size
        # size의 갯수만큼 모듈로Modulo 연산을 한 나머지를 해시값으로 정하는 단순한 형태로 처리
        # 모듈로 연산을 통한 해싱은 해시 테이블의 가장 기본적인 방식
        # 해싱 결과인 index는 해시 테이블의 인덱스
        if self.table[index].value is None:
            # value의 존재 유무 ? 
            # defaultdict -> 존재하지 않는 인덱스를 조회할 경우 빈 listnode 생성(상단 두개의 init 참고), key, value = none
            self.table[index] = ListNode(key, value)
            return
        
        # 해당 인덱스에 노드가 존재하는 경우 = Hash Collision이 발생할 경우
        # 개별 체이닝 방식으로 충돌 해결
        p = self.table[index]
        while p:
            if p.key == key:
            # 키가 존재하면 값을 업데이트
                p.value = value
                return
            if p.next is None:
            # 이를 처리하지 않으면, p=p.next로 인해, p는 none이 됨
                break
            p = p.next
        p.next = ListNode(key, value)
        # 새 노드가 생성되면서 연결된다.
        # 즉, 개별 체이닝 방식의 해시 테이블 삽입 원리

    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
            # 탐색하면서 일치하는 키를 찾음
        return -1


    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫번 째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


hashMap = MyHashMap()
hashMap
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)
hashMap.get(2)
hashMap.put(2, 3)
hashMap.get(2)
hashMap.remove(2)
hashMap.get(2)