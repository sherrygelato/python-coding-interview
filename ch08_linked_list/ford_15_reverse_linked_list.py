#!/usr/bin/python3
"""
CH08. 15_Reverse_Linked_List.py
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# 입력
# 1->2->3->4->5->NULL
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# 출력
# 5->4->3->2->1->NULL

# --------------------------------------------------
def reverseList(head):
    def reverse(node, prev = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    
    return reverse(head)


result = reverseList(node1)

while result:
    print(result.val, end = ' ')
    result = result.next


# --------------------------------------------------
def reverseList2(head):
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
        
    return prev


result = reverseList2(node1)

while result:
    print(result.val, end = ' ')
    result = result.next
