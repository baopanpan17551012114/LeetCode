#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

"""
给你 k 种⾯值的硬币，⾯值分别为 c1, c2 ... ck，每种硬币的数量⽆限，再给⼀个总⾦额 amount，
问 你最少需要⼏枚硬币凑出这个⾦额，如果不可能凑出，算法返回 -1

⽐如说 k = 3 ，⾯值分别为 1，2，5，总⾦额 amount = 11 。那么最少需 要 3 枚硬币凑出，即 11 = 5 + 5 + 1。
"""


# 递归解法
def get_recursion(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    result = np.Inf
    for coin in coins:
        # 计算子问题的结果
        pre_value = get_recursion(coins, amount - coin)
        # 子问题无解则跳过
        if pre_value == -1:
            continue
        # 在子问题中选择最优解
        result = min(result, pre_value+1)
    return result


# dp
def get_dp(coins, amount):
    if amount < 0:
        return -1

    dp = [amount+1]*(amount+1)
    dp[0] = 0
    # 求最小值，初始化为正无穷
    for i in range(amount+1):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[-1]


if __name__ == '__main__':
    res = get_recursion([1, 2, 5], 11)
    print(res)
    res = get_dp([1, 2, 5], 11)
    print(res)
