#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗二叉树。

示例 1:
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(inorder, postorder)

    def build(self, inorder, postorder):
        if len(inorder) == 0:
            return None

        value = postorder[-1]
        inorder_index = inorder.index(value)

        root = TreeNode(value)
        root.left = self.build(inorder[0:inorder_index], postorder[0:inorder_index])
        root.right = self.build(inorder[inorder_index+1:], postorder[inorder_index:-1])

        return root
