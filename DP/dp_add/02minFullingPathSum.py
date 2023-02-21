#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
输⼊为⼀个 n * n 的⼆维数组 matrix，请你计算从第⼀⾏落到最 后⼀⾏，经过的路径和最⼩为多少
你可以站在 matrix 的第⼀⾏的任意⼀个元素，需要下降到最后⼀⾏。
每次下降，可以向下、向左下、向右下三个⽅向移动⼀格。也就是说，可以从 matrix[i][j] 降到
matrix[i+1][j] 或 matrix[i+1][j-1] 或 matrix[i+1][j+1] 三个位置。 请你计算下降的「最⼩路径和」
示例：
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
输出： 13
path: 1-5-7, 1-4-8
"""
import numpy as np


def get_recursion(matrix):
    # 递归
    def recursion(matrix, i, j):
        if i == 0:
            return matrix[i][j]
        left = recursion(matrix, i-1, j-1) if j-1 >= 0 else np.Inf
        right = recursion(matrix, i-1, j+1) if j+1 <= len(matrix)-1 else np.Inf
        return min(recursion(matrix, i-1, j), left, right) + matrix[i][j]

    res = np.Inf
    for j in range(len(matrix)):
        res = min(res, recursion(matrix, len(matrix)-1, j))
    return res


def get_dp(matrix):
    n = len(matrix)
    # base case
    dp = [matrix[0]]
    for i in range(1, n):
        dp.append([0] * n)

    # 状态：dp[i][j]中的值，也就是路径和
    # 选择；行i和列j的变化
    for i in range(1, n):  # 每一行
        for j in range(n):
            # 状态转移方程
            left = dp[i-1][j-1] if j > 0 else np.Inf
            high = dp[i-1][j]
            right = dp[i-1][j+1] if j < n-1 else np.Inf
            dp[i][j] = min(left, high, right) + matrix[i][j]
    return min(dp[-1])


if __name__ == '__main__':
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    re = get_dp(matrix)
    print(re)
    matrix = [[2]]
    re = get_dp(matrix)
    print(re)

    # 递归
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    re = get_recursion(matrix)
    print(re)
    matrix = [[2]]
    re = get_recursion(matrix)
    print(re)

    """
    类似于从左上角到右下角最短路径问题
    dp数组和贪心法到区别在于：dp[i][j]存放了当前位置最小值，而一旦第i行的值确定，则i+1行中各列的值可以递推出来
    贪心法则保存的不是二维数组，第一行选择最小的数，然后初始位置就确定了
    """