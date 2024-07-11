#!/usr/bin/env python
# -*- coding:utf-8 -*-\

"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
你可以认为每种硬币的数量是无限的。


示例1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
"""
import sys
from typing import List
import numpy as np


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp表示amount需要的最少硬币个数
        dp = [0] * (amount+1)
        # base case
        if amount < 0:
            return -1
        dp[0] = 0
        for i in range(1, amount+1):
            value = np.Inf
            for coin in coins:
                pre_value = dp[i - coin] + 1 if i >= coin else np.Inf
                value = min(pre_value, value)
            dp[i] = value
        return dp[-1] if dp[-1] != np.Inf else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [np.Inf] * (amount+1)
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if memo[amount] != np.Inf:
            return memo[amount]
        res = np.Inf
        for coin in coins:
            pre_value = self.coinChange(coins, amount-coin)
            if pre_value == -1:
                continue
            res = min(res, pre_value+1)
        result = res if res != np.Inf else -1
        memo[amount] = result
        return result


if __name__ == '__main__':
    coins = [2]
    amount = 4
    res = Solution1().coinChange(coins, amount)
    print(res)
