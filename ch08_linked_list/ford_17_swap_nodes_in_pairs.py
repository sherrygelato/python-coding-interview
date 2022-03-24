#!/usr/bin/python3
"""
CH08. 17_Swap_Nodes_in_Pairs.py
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# 입력
# 1->2->3->4
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

# 출력
# 2->1->4->3

# --------------------------------------------------
def swapPairs(head):
    cur = head
    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head

result = swapPairs(node1)

while result:
    print(result.val, end = ' ')
    result = result.next


# --------------------------------------------------
def swapPairs2(head):
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # a->b에서 b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head
        
        # prev가 b를 가리키도록 할당
        prev.next = b
        
        # 다음 스왑을 위해 이동
        head = head.next
        prev = prev.next.next
    
    return root.next


result = swapPairs2(node1)

while result:
    print(result.val, end = ' ')
    result = result.next


# --------------------------------------------------
def swapPairs3(head):
    if head and head.next:
        p = head.next
        print(head.next.val)
        
        head.next = swapPairs3(p.next)
        p.next = head
        print(p.val)
        return p
    return head


result = swapPairs3(node1)

while result:
    print(result.val, end = ' ')
    result = result.next


# --------------------------------------------------