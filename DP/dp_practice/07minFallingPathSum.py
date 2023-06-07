#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一个 n x n 的 方形 整数数组matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1)

输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
"""
from typing import List

import numpy as np


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        # base case
        for i in range(len(matrix[0])):
            dp[0][i] = matrix[0][i]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                left_value = dp[i-1][j-1] if j>0 else np.Inf
                value = dp[i-1][j]
                right_value = dp[i-1][j+1] if j+1<len(matrix[0]) else np.Inf
                dp[i][j] = min(left_value, value, right_value) + matrix[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    # matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    matrix = [[17, 82], [1, -44]]
    res = Solution().minFallingPathSum(matrix)
    print(res)