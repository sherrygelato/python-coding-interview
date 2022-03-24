#!/usr/bin/python3
"""
CH08. 14_Merge_Two_Sorted.py
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# 입력
# 1->2->4, 1->3->4
node1 = ListNode(1)
node11 = ListNode(2)
node12 = ListNode(4)
node1.next = node11
node11.next = node12

node2 = ListNode(1)
node21 = ListNode(3)
node22 = ListNode(4)
node2.next = node21
node21.next = node22

# 출력
# false

# --------------------------------------------------
def mergeTwoLists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1


result = mergeTwoLists(node1, node2)

while result:
    print(result.val, end = ' ')
    result = result.next
