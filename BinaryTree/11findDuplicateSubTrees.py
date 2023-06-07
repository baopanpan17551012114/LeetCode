#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一棵二叉树的根节点 root ，返回所有 重复的子树 。
对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。
如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。

示例 1：
输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]
"""

# Definition for a binary tree node.
import copy
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.tree_dict = {}
        self.total_list = []
        self.find(root)
        print(self.tree_dict)
        return self.tree_dict.values()

    def find(self, root):
        if root is None:
            return '#'
        left_child = self.find(root.left)
        right_child = self.find(root.right)
        # 获取前序排序结果
        # 输出：[[11,1]]
        pre_order = str(root.val) + left_child + right_child  # [2,1,11,11,null,1]
        # pre_order = str(root.val) + '(' + left_child + ')' + right_child  # 这两个区别是啥
        if pre_order in self.total_list and self.tree_dict.get(pre_order, None) is None:
            self.tree_dict[pre_order] = root
        self.total_list.append(pre_order)
        return pre_order


if __name__ == '__main__':
    root = TreeNode(2)
    node1 = TreeNode(1)
    node2 = TreeNode(11)
    node3 = TreeNode(11)
    node4 = TreeNode(1)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    res = Solution().findDuplicateSubtrees(root)
    print(res)


