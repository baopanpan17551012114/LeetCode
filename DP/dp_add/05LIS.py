#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
输⼊⼀个⽆序的整数数组，请你找到其中最⻓的严格递增⼦序列的⻓度
⽐如说输⼊ nums=[10,9,2,5,3,7,101,18]，其中最⻓的递增⼦序列是 [2,3,7,101]，所以算法的输出 应该是 4。
注意「⼦序列」和「⼦串」这两个名词的区别，⼦串⼀定是连续的，⽽⼦序列不⼀定是连续的。
"""
import numpy as np


def get_recursion(nums):
    # base case
    pass


def get_dp(nums):
    dp = [0] * len(nums)
    # base case
    dp[0] = 1
    # dp表示：以nums[i]为结尾的子串长度
    for i in range(1, len(nums)):
        res = 0
        for j in range(i):
            if nums[i] > nums[j]:
                res = max(res, dp[j])
        dp[i] = res + 1
    return max(dp)


if __name__ == '__main__':
    result = get_dp([10, 9, 2, 5, 3, 7, 101, 18])
    print(result)