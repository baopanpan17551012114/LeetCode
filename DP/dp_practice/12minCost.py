#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。
每个房子粉刷成不同颜色的花费是以一个n x 3的正整数矩阵 costs 来表示的。
例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2]表示第 1 号房子粉刷成绿色的花费，以此类推。
请计算出粉刷完所有房子最少的花费成本。


示例 1：
输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
输出: 10
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
最少花费: 2 + 5 + 3 = 10。
"""
from typing import List

import numpy as np


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0 for i in range(3)] for j in range(len(costs))]
        # base case
        for i in range(3):
            dp[0][i] = costs[0][i]
        for i in range(1, len(costs)):
            for j in range(3):
                left = dp[i-1][j-1] if j-1>=0 else np.Inf
                left1 = dp[i - 1][j - 2] if j - 2 >= 0 else np.Inf
                right = dp[i-1][j+1] if j+1<3 else np.Inf
                right1 = dp[i - 1][j + 2] if j + 2 < 3 else np.Inf
                dp[i][j] = min(left, right, left1, right1) + costs[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    costs = [[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]
    res = Solution().minCost(costs)
    print(res)