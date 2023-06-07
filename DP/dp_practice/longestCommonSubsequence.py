#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)
        dp = [[0 for i in range(N)] for j in range(M)]
        # dp[m][n]表示以 text1[m] 和text2[n]结尾的公共子序列长度
        # base case
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for m in range(1, M):
            dp[m][0] = int(text1[m] == text2[0] or dp[m-1][0])
        for n in range(1, N):
            dp[0][n] = int(text1[0] == text2[n] or dp[0][n-1])

        for m in range(1, M):
            for n in range(1, N):
                if text1[m] == text2[n]:
                    dp[m][n] = dp[m - 1][n - 1] + 1
                else:
                    dp[m][n] = max(dp[m-1][n], dp[m][n-1])
        return dp[-1][-1]


if __name__ == '__main__':
    # text1 = "abcde"
    # text2 = "ace"
    text1 = "bl"
    text2 = "yby"

    res = Solution().longestCommonSubsequence(text1, text2)
    print(res)