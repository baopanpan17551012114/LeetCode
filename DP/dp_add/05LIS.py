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


def double_point(nums):
    left_index = 0
    right_index = 0
    length_res = 0
    while right_index <= len(nums)-1:
        if nums[right_index+1] < nums[right_index]:
            length_res = max(left_index, right_index-left_index)
            left_index = right_index + 1
            right_index = left_index + 1
        else:
            right_index += 1
    length_res = max(length_res, right_index-left_index)
    print(length_res)


if __name__ == '__main__':
    result = get_dp([10, 9, 2, 5, 3, 7, 101, 18])
    print(result)
    double_point([10, 9, 2, 5, 3, 7, 101, 18])

    # 最长递增子序列长度: