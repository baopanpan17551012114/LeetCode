#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

"""
0-1 背包问题。描述：
给你⼀个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
其中第 i 个物品的重量为wt[i]，价值为 val[i]，现在让你⽤这个背包装物品，最多能装的价值是多少？
N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
返回 6，选择前两件物品装进背包，总重量 3 ⼩于 W，可以获得最⼤价值6
"""


def get_dp(n, w, wt, val):
    """
    dp为二维数组，N * W dp[i][j]表示对于前 i 个物品，当前背包的容量为 j，这种情况下可以装的最⼤价值是 dp[i][j]
    :param n:
    :param w:
    :param wt:
    :param val:
    :return:
    """
    dp = [[0 for j in range(w+1)] for i in range(n+1)]
    # base case, 0行 0列都为0，不用操作
    for i in range(1, n+1):
        for j in range(1, w+1):
            # wt[i-1]表示第i个物品重量，val[i-1]表示第i个物品价值
            # 状态： 背包容量 和 可选择的物品
            # 选择有两种：不更换 或 更换
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i-1]]+val[i-1] if j-wt[i-1] >= 0 else -np.Inf)

    print(dp[-1][-1])


if __name__ == '__main__':
    get_dp(3, 4, [2, 1, 3], [4, 2, 3])
