#!/usr/bin/python3
"""
CH08. 13_Palindrome_Linked_List.py
"""


class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# 입력 1
# 1->2
node11 = ListNode(1)
node12 = ListNode(2)
node11.next = node12

# 출력 1
# false

# 입력 2
# 1->2->2->1
node21 = ListNode(1)
node22 = ListNode(2)
node23 = ListNode(2)
node24 = ListNode(1)
node21.next = node22
node22.next = node23
node23.next = node24


# 출력 2
# true

# --------------------------------------------------
def isPalindrome(head):
    q = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


print(isPalindrome(node11))
print(isPalindrome(node21))


# --------------------------------------------------
from collections import deque

def isPalindrome2(head):
    q = deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
        
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
        
    return True


print(isPalindrome2(node11))
print(isPalindrome2(node21))


# --------------------------------------------------
def isPalindrome3(head):
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
        
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev 


print(isPalindrome3(node11))
print(isPalindrome3(node21))


# --------------------------------------------------
