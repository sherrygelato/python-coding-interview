"""
CH10. 26_Design_Circular_Deque.py
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


# --------------------------------------------------
class MyCircularDeque:
    def __init__(self, length):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.length, self.len = length, 0
        self.head.right, self.tail.left = self.tail, self.head


    def _add(self, node, new):
        tmp = node.right
        node.right = new
        new.left, new.right = node, tmp
        tmp.left = new


    def _del(self, node):
        tmp = node.right.right
        node.right = tmp
        tmp.left = node


    def insertFront(self, value):
        if self.len == self.length:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True


    def insertLast(self, value):
        if self.len == self.length:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True


    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True


    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True


    def getFront(self):
        return self.head.right.val if self.len else -1


    def getRear(self):
        return self.tail.left.val if self.len else -1


    def isEmpty(self):
        return self.len == 0


    def isFull(self):
        return self.len == self.length


# --------------------------------------------------
deque = MyCircularDeque(10)
deque.insertFront(3)
deque.insertFront(2)
deque.insertFront(1)

deque.insertLast(6)
deque.insertLast(7)
deque.insertLast(8)

deque.deleteFront()
deque.deleteFront()

deque.deleteLast()
deque.deleteLast()

deque.getFront()
deque.getRear()

deque.isEmpty()
deque.isFull()