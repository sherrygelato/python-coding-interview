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
import functools

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
    
    """숫자형 합치기"""
    # resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
    # resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))
    resultStr = functools.reduce(lambda x, y: 10*x + y, a) + functools.reduce(lambda x, y: 10*x + y, b)
    
    return toReversedLinkedList(str(resultStr))


result = addTwoNumbers(node1, node2)

while result:
    print(result.val, end = ' ')
    result = result.next


# --------------------------------------------------
def addTwoNumbers2(l1, l2):
    root = head = ListNode(0)
    
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
            
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next
    
    return root.next


result = addTwoNumbers2(node1, node2)

while result:
    print(result.val, end = ' ')
    result = result.next