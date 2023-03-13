#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你输⼊⼀个整数数组 nums，请你找在其中找⼀个和最⼤的⼦数组，返回这个⼦数组的和
 nums = [-3,1,3,-1,2,-4,2]，算法返回 5，因为最⼤⼦数组 [1,3,-1,2] 的和为 5。
"""
import numpy as np


def get_dp(nums):
    """
    当前值+之前序列 > 0, 加入
    :param nums:
    :return:
    """
    dp = [-np.Inf] * len(nums)
    # base case
    dp[0] = nums[0]
    # dp表示：以dp[i-1]为结尾的子数组的和
    for i in range(1, len(nums)):
        dp[i] = max(nums[i] + dp[i-1], nums[i])
    print(max(dp))
    """优化: 不用保存整个dp"""


if __name__ == '__main__':
    nums = [-3, 1, 3, -1, 2, -4, 2]
    get_dp(nums)