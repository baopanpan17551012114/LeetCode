#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一个下标从 0 开始的整数数组 nums和一个整数 k。

一开始你在下标0处。每一步，你最多可以往前跳k步，但你不能跳出数组的边界。也就是说，你可以从下标i跳到[i + 1， min(n - 1, i + k)]包含 两个端点的任意位置。
你的目标是到达数组最后一个位置（下标为 n - 1），你的 得分为经过的所有数字之和。
请你返回你能得到的 最大得分。

示例 1：

输入：nums = [1,-1,-2,4,-7,3], k = 2
输出：7
解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7。

"""
from typing import List
import numpy as np


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # base case
        dp = [0] * len(nums)
        if len(nums) < 3:
            return sum(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            pre = -np.Inf
            for j in range(k):
                pre_value = dp[i-1-j] if i-1-j > -1 else -np.Inf
                pre = max(pre, pre_value)
            dp[i] = pre + nums[i]
        return dp[-1]


if __name__ == '__main__':
    nums = [1, -1, -2, 4, -7, 3]
    k = 2
    res = Solution().maxResult(nums, k)
    print(res)