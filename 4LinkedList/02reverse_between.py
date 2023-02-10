#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        origin_root = head
        origin_last = None
        right_first = None
        reversed_last = None
        x = 0
        new_root = None
        while head != None:
            x += 1
            if x>=m and x<=n:
                if x == m:
                    reversed_last = head
                first = head
                second = head.next
                first.next = new_root
                new_root = first
                head = second
            else:
                if x == n+1:
                    right_first = head
                    break
                if x < m:
                    origin_last = head
                    head = head.next
        if reversed_last != None:
            reversed_last.next = right_first
        if origin_last != None:
            origin_last.next = new_root
        else:
            return new_root

        return origin_root

