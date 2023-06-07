#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。
题目数据保证答案符合 32 位带符号整数范围。

示例1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len1 = len(s)
        len2 = len(t)
        dp = [[0 for j in range(len2)] for i in range(len1)]
        # base case
        if s[0] == t[0]:
            dp[0][0] = 1
        for i in range(1, len1):
            if s[i] == t[0]:
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, len1):
            for j in range(1, len2):
                if s[i] != t[j]:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 母串使用最后一个字符，母串不使用最后一个字符
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    Solution().numDistinct(s, t)