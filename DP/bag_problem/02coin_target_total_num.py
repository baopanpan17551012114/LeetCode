#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
完全背包问题
给定不同⾯额的硬币 coins 和⼀个总⾦额 amount，写⼀个函数来计算可以凑成总⾦额的硬币组合数。假设 每⼀种⾯额的硬币有⽆限个。
amount = 5, coins = [1,2,5]，算法应该返回 4，
amount = 5, coins = [3]，算法应该返回 0
"""


def get_dp(amount, coins):
    # 状态：目标金额，coin
    # 选择：用或者不用指定面额coin
    # dp[i][j]表示目标金额为j时,只用前i个硬币的组合数
    dp = [[0 for i in range(amount + 1)] for j in range(len(coins)+1)]
    # base case
    # 第一列为1
    for i in range(len(coins)+1):
        dp[i][0] = 1
    for i in range(1, len(coins)+1):
        for j in range(1, amount+1):
            dp[i][j] = dp[i-1][j] + (dp[i][j-coins[i-1]] if j-coins[i-1] >= 0 else 0)
    print(dp[-1][-1])


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    get_dp(amount, coins)
