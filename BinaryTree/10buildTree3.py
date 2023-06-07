#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个整数数组，preorder和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。

如果存在多个答案，您可以返回其中 任何 一个。

示例 1：
输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, postorder)

    def build(self, preorder, postorder):
        if len(preorder) == 0:
            return None

        value = preorder[0]
        root = TreeNode(value)

        # 找到最短前、后遍历有相同子集的列表
        index = 0
        for i in range(1, len(preorder)):
            pre = preorder[1:i+1]
            post = postorder[0:i]
            if self.is_same(pre, post):
                index = i
                break
        root.left = self.build(preorder[1:index+1], postorder[:index])
        root.right = self.build(preorder[index + 1:], postorder[index:-1])
        return root

    def is_same(self, pre, post):
        for ele in pre:
            if ele not in post:
                return False
        return True
