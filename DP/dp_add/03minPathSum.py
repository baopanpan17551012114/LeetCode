#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
输⼊为⼀个 n * n 的⼆维数组 matrix，从左上角到右下角，经过的路径和最⼩为多少，每次向下或向右移动
示例：
matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
输出： 7

matrix = [[1, 2, 3], [4, 5, 6]]
输出： 12
"""
import copy

import numpy as np


def get_recursion(matrix):
    """
    递归方法解决
    :param matrix:
    :return:
    """
    def recursion(matrix, i, j):
        if i == 0:
            return sum([matrix[0][k] for k in range(j+1)])
        if j == 0:
            return sum([matrix[k][0] for k in range(i+1)])
        up_value = recursion(matrix, i-1, j) if i > 0 else np.Inf
        left_value = recursion(matrix, i, j-1) if j > 0 else np.Inf

        return min(up_value, left_value) + matrix[i][j]

    result = recursion(matrix, len(matrix)-1, len(matrix[0])-1)
    return result


def get_dp(matrix):
    dp = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0:
                dp[i][j] = (dp[i][j-1] + dp[i][j]) if j > 0 else dp[i][j]  # base case
            elif j == 0:
                dp[i][j] = (dp[i-1][j]) + dp[i][j] if i > 0 else dp[i][j]
            else:
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])  # 状态转移
    return dp[-1][-1]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    result = get_recursion(matrix)
    print(result)

    matrix = [[1, 2, 3], [4, 5, 6]]
    result = get_dp(matrix)
    print(result)