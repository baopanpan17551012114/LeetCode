#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你输⼊两个字符串 s1 和 s2，请你找出他们俩的最⻓公共⼦序列，返回这个⼦序列的⻓度。
输⼊ s1 = "zabcde", s2 = "acez"，它俩的最⻓公共⼦序列是 lcs = "ace"，⻓度为 3，所以 算法返回 3。
"""
import numpy as np


def get_double_index(s1, s2):
    pass


def get_dp(s1, s2):
    """
    子序列不连续
    dp数组为二维， 定义为以s1[i] 和 s2[j] 为结尾的最长公共子序列长度
    if s1[i] == s2[j], dp[i-1][j-1] + 1
    或者 max(dp[i-1][j], dp[i][j-1])
    :param s1:
    :param s2:
    :return:
    """
    dp = [[0 for i in range(len(s2))] for j in range(len(s1))]
    # base case
    dp[0][0] = 1 if s1[0] == s2[0] else 0
    for j in range(1, len(s2)):
        if s1[0] == s2[j]:
            dp[0][j] = dp[0][j-1] + 1
        else:
            dp[0][j] = dp[0][j - 1]

    for i in range(1, len(s1)):
        if s1[i] == s2[0]:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            tmp1 = -np.Inf
            if s1[i] == s2[j]:
                tmp1 = dp[i-1][j-1] + 1
            tmp2 = dp[i-1][j]
            tmp3 = dp[i][j-1]
            dp[i][j] = max(tmp1, tmp2, tmp3)
    print(dp[-1][-1])


if __name__ == '__main__':
    s1 = "zabcde"
    s2 = "acez"
    get_dp(s1, s2)
