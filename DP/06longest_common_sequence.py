#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
最长公共子序列
题目描述：
给定两个字符串A和B，同时给定两个串的长度n和m，请返回最长公共子序列的长度。保证两串长度均小于等于300。
给定两个字符串，求解这两个字符串的最长公共子序列（Longest Common Sequence）。比如字符串1：BDCABA；字符串2：ABCBDAB
则这两个字符串的最长公共子序列长度为4，最长公共子序列是：BCBA

最长公共连续子串
最长公共连续子串。与序列不同，子串要求字符是连续的，而子序列可以不连续。

3.3最大连续子序列和
对于一个有正有负的整数数组，请找出总和最大的连续数列。
测试样例：
[1,2,3,-6,1]
返回：6
"""


def get_longest_common_sequence(str1, str2):
    # dp[i-1][j-1] + 1
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = 1 if str1[0] == str2[0] else 0
    for i in range(1, n):
        dp[0][i] = int((str2[i] == str1[0]) or dp[0][i-1])
    for j in range(1, m):
        dp[j][0] = int((str1[j] == str2[0]) or dp[j-1][0])

    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])


def get_longest_sub_sequence(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = 1 if str1[0] == str2[0] else 0
    for i in range(1, n):
        dp[0][i] = int((str2[i] == str1[0]) or dp[0][i - 1])
    for j in range(1, m):
        dp[j][0] = int((str1[j] == str2[0]) or dp[j - 1][0])

    # dp[i-1][j-1]代表以str1[i]和str2[j]分别为结尾字符时的最长
    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
    print(dp)


if __name__ == '__main__':
    get_longest_common_sequence("ezupkr", "ubmrapg")
    # get_longest_sub_sequence('ABCBDAB', 'BDCABA')


