#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
假设有几种硬币，如1、3、5，并且数量无限。请找出能够组成某个数目的找零所使用最少的硬币数。
"""


def coin_dispenser_min(n):
    """dp[n] = min(dp[n-1]+1, dp[n-3]+1, dp[n-5]+1)"""
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(1, n):
        if i < 3:
            dp[i] = dp[i-1]+1
        elif 3 <= i < 5:
            dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1)
        else:
            dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1, dp[i - 5] + 1)
    print(dp)

if __name__ == '__main__':
    coin_dispenser_min(15)
