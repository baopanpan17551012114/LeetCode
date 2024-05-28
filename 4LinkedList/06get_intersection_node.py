# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left = headA
        right = headB
        while left and right:
            left = left.next
            right = right.next
        m = headA
        n = headB
        if left:
            left = left.next
            m = m.next
        if right:
            right = right.next
            n = n.next
        while m != n:
            m = m.next
            n = n.next
            if n is None or m is None:
                return None
        return m


if __name__ == '__main__':
    # [1,9,1,2,4]
    # [3,2,4]
    l1 = ListNode(1)
    l2 = ListNode(9)
    l3 = ListNode(1)
    l4 = ListNode(2)
    l5 = ListNode(4)

    l6 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    l6.next = l4

    res = Solution().getIntersectionNode(l1, l6)
    print(res)