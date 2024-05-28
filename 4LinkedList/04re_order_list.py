from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 先获取后半截链表，再翻转，再合并
        def reverse(root):
            new_head = None
            cur = nxt = root  # cur和nxt指向同一个节点
            while cur is not None:
                nxt = nxt.next
                cur.next = new_head
                new_head = cur
                cur = nxt
            return new_head

        def get_half_list(root):
            fast = low = root
            while fast is not None:
                fast = fast.next
                if fast:
                    fast = fast.next
                if fast:
                    low = low.next
            return low

        half_end = get_half_list(head)
        half_root = half_end.next
        half_end.next = None
        new_half_root = reverse(half_root)
        # 交替拼接
        cur = head
        left_index = head.next
        right_index = new_half_root
        while (left_index is not None) and (right_index is not None):
            cur.next = right_index
            right_index = right_index.next
            cur = cur.next
            cur.next = left_index
            cur = cur.next
            left_index = left_index.next
        if left_index is not None:
            cur.next = left_index
        if right_index is not None:
            cur.next = right_index
