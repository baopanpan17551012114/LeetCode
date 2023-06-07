#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个不重复的整数数组nums 。最大二叉树可以用下面的算法从nums 递归地构建:

创建一个根节点，其值为nums 中的最大值。
递归地在最大值左边的子数组前缀上构建左子树。
递归地在最大值 右边 的子数组后缀上构建右子树。
返回nums 构建的 最大二叉树 。
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build_tree(nums)

    def build_tree(self, nums):
        if len(nums) == 0:
            return None
        max_value = max(nums)
        index = nums.index(max_value)
        root = TreeNode(max_value)
        root.left = self.build_tree(nums[0:index])
        root.right = self.build_tree(nums[index+1:])

        return root
