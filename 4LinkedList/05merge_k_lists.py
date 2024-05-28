# Definition for singly-linked list.
import sys
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        cur = root_pre = ListNode(-1)
        while True:
            min_node_index = None
            for node in lists:
                print(lists.index(node), "*"*10)
                print(node.val)
                if node:
                    if not min_node_index:
                        min_node_index = node
                    else:
                        if node.val < min_node_index.val:
                            min_node_index = node
            if min_node_index is None:
                return root_pre.next
            else:
                cur.next = min_node_index
                min_node_index = min_node_index.next  # 这里不生效
                cur = cur.next
                cur.next = None

if __name__ == '__main__':
    # [[1,4,5],[1,3,4],[2,6]]
    l11 = ListNode(1)
    l12 = ListNode(4)
    l13 = ListNode(5)
    l11.next = l12
    l11.next.next = l13

    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l21.next = l22
    l21.next.next = l23

    l31 = ListNode(2)
    l32 = ListNode(6)
    l31.next = l32
    node_list = [l11, l21, l31]
    res = Solution().mergeKLists(node_list)
    print(res.val)