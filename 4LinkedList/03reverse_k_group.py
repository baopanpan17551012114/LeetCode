#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表
如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样
你不能更改节点中的值，只能更改节点本身。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverse(self, a, b):
        current_node = a
        current_next_node = a
        new_head = None
        while current_node != b:
            current_next_node = current_node.next
            current_node.next = new_head
            new_head = current_node
            current_node = current_next_node
        return new_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        a, b = head, head
        for i in range(k):
            if b is None:
                return a
            b = b.next  # 如果放在if之前, 那么最后正好k个的话会不做反转操作

        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
