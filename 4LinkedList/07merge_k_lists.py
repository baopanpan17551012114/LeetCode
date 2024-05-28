from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 新建一个list存储所有链表的值
        heap = []
        # 遍历lists中所有链表的值，逐个加入到heap列表中
        for sub_list in lists:
            while sub_list:
                heap.append(sub_list.val)
                sub_list = sub_list.next
        # 对heap进行降序排序
        heap.sort(reverse=True)
        # 新建一个链表
        head = ListNode(None)
        curr_list = head
        while heap:
            # 从heap列表的尾部取最小数加入到链表中
            temp_list = ListNode(heap.pop())
            curr_list.next = temp_list
            curr_list = curr_list.next
        return head.next

# 包heapq最小堆

if __name__ == '__main__':
    pass
