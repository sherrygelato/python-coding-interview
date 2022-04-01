"""
CH10. 28_Design_HashMap.py
"""
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect

# --------------------------------------------------
class ListNode:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self, size = 1000):
        self.size = size
        self.table = collections.defaultdict(ListNode)


    def put(self, key, value):
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1


    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

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
