#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""反转列表"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        new_root = None
        while head != None:
            first = head
            second = head.next
            first.next = new_root
            new_root = first
            head = second
        return new_root


