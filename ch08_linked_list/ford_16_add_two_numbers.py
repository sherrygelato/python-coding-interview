#!/usr/bin/python3
"""
CH08. 16_Add_Two_Numbers.py
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# 입력
# 1->2->4, 1->3->4
node1 = ListNode(2)
node11 = ListNode(4)
node12 = ListNode(3)
node1.next = node11
node11.next = node12

node2 = ListNode(5)
node21 = ListNode(6)
node22 = ListNode(4)
node2.next = node21
node21.next = node22


# 출력
# 7->0->8

# 설명
# 342 + 465 = 807 

# --------------------------------------------------
def reverseList(head):
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
        
    return prev


def toList(node):
    list = []
    while node:
        list.append(node.val)
        node = node.next
    return list


def toReversedLinkedList(result):
    prev = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
        
    return node


def addTwoNumbers(l1, l2):
    a = toList(reverseList(l1))
    b = toList(reverseList(l2))
    
    resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
    
    return toReversedLinkedList(str(resultStr))


result = addTwoNumbers(node1, node2)

while result:
    print(result.val, end = ' ')
    result = result.next


# --------------------------------------------------
