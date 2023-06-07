#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历， inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, inorder)

    def build(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        value = preorder[0]
        inorder_index = inorder.index(value)
        root = TreeNode(value)
        root.left = self.build(preorder[1:1+inorder_index], inorder[0:inorder_index])
        root.right = self.build(preorder[1+inorder_index:], inorder[inorder_index+1:])

        return root
