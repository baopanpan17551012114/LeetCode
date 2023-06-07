#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# 遍历思维
class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse(root)
        return root

    def reverse(self, root):
        if root is None:
            return
        root.right, root.left = root.left, root.right
        self.reverse(root.right)
        self.reverse(root.left)

# 分治思维
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

