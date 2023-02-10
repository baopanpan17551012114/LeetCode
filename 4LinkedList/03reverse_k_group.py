#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表
如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样
你不能更改节点中的值，只能更改节点本身。"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverse_k_group(self, head_start, head_end):
        new_root_start = None
        new_root_end = head_start
        while head_start != head_end:
            first = head_start
            second = head_start.next
            head_start.next = new_root_start
            new_root_start = first
            head_start = second
        first = head_end
        first.next = new_root_start
        new_root_start = first
        return new_root_start, new_root_end

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # write code here
        if k == 1:
            return head
        total_start = head
        total_end = None
        root = head
        origin_next = None
        tmp_start = head
        tmp_end = head
        index = 0
        while head != None:
            second = head.next
            index += 1
            if index % k == 0:
                if tmp_start != root:
                    tmp_start = origin_next
                tmp_end = head
                list_start, list_end = self.reverse_k_group(tmp_start, tmp_end)
                tmp_start = None
                if total_start == root:
                    total_start = list_start
                    total_end = list_end
                else:
                    total_end.next = list_start
                    total_end = list_end
                origin_next = second
            head = second
        if origin_next != None:
            total_end.next = origin_next
        return total_start


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    root = l1
    re = Solution().reverseKGroup(l1, 2)
    while re!=None:
        print(re.val, end=" ")
        re = re.next

