#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
⽐如说 k = 3 ，⾯值分别为 1，2，5，总⾦额 amount = 11 。那么最少需 要 3 枚硬币凑出，即 11 = 5 + 5 + 1。
"""


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
    print(dp)
    return dp[-1]


if __name__ == '__main__':
    res = get_dp([1, 2, 5], 0)
    print(res)
