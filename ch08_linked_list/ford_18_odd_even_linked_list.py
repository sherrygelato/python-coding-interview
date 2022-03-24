#!/usr/bin/python3
"""
CH08. 18_Odd_Even_Linked_List.py
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# 입력 1
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

# 출력 1
# 1->3->5->2->4->NULL

# 입력 2
# 2->1->3->5->6->4->7NULL
node01 = ListNode(2)
node02 = ListNode(1)
node03 = ListNode(3)
node04 = ListNode(5)
node05 = ListNode(6)
node06 = ListNode(4)
node07 = ListNode(7)
node01.next = node02
node02.next = node03
node03.next = node04
node04.next = node05
node05.next = node06
node06.next = node07

# 출력 2
# 2->3->6->7->1->5->4NULL

# --------------------------------------------------
def oddEvenList(head):
    if head is None:
        return None
    
    odd = head
    even = head.next
    even_head = head.next
    
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
        
    odd.next = even_head
    return head


result = oddEvenList(node1)
result2 = oddEvenList(node01)

while result:
    print(result.val, end = ' ')
    result = result.next
print('\n---')
while result2:
    print(result2.val, end = ' ')
    result2 = result2.next