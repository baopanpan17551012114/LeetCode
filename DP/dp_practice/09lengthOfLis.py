#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp表示以nums[i]为结尾的子序列 最长严格递增子序列的长度
        dp = [0 for i in range(len(nums))]
        # base case
        dp[0] = 1
        for i in range(1, len(nums)):
            res = 1
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                else:
                    res = max(res, dp[j]+1)
            dp[i] = res
        return max(dp)


if __name__ == '__main__':
    nums = [1,3,6,7,9,4,10,5,6]

    res = Solution().lengthOfLIS(nums)
    print(res)