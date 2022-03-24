#!/usr/bin/python3
"""
CH08. 19_Reverse_Linked_List_2.py
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# 입력
# 1->2->3->4->5->NULL, m = 2, n = 4
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
# 1->4->3->2->5->NULL

# --------------------------------------------------
def reverseBetween(head, m, n):
    if not head or m == n:
        return head
    
    root = start = ListNode(None)
    root.next = head
    
    for _ in range(m-1):
        start = start.next
    end = start.next
    
    for _ in range(n-m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next

result = reverseBetween(node1, 2, 4)

while result:
    print(result.val)
    result = result.next