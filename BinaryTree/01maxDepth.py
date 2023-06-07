#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明:叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth = 0
        self.traverse(root)
        return self.res

    # 遍历思路，回溯法
    def traverse(self, root: TreeNode):
        if root is None:
            return
        # 前序位置
        self.depth += 1
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置
        self.depth -= 1


# 分治思路，动态规划
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)
        return max(left_length, right_length) + 1


