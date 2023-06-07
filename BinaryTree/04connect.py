#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有next 指针都被设置为 NULL。
"""

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# 层次遍历
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        node_list = []
        node_list.append(root)
        while len(node_list) != 0:
            size = len(node_list)
            tmp_list = []
            for i in range(size):
                if node_list[i] is not None and node_list[i].left is not None:
                    tmp_list.append(node_list[i].left)
                    tmp_list.append(node_list[i].right)
                if i == size - 1:
                    break
                node_list[i].next = node_list[i+1]
            node_list = tmp_list

        return root
