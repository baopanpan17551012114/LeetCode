#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定三个字符串s1、s2、s3，请你帮忙验证s3是否是由s1和s2交错组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
"""
import datetime
import time


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0] = True
        # base case
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, len(s2)+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                p = i + j - 1
                dp[i][j] = (s1[i-1] == s3[p] and dp[i-1][j]) or (s2[j-1] == s3[p] and dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    res = Solution().isInterleave(s1, s2, s3)
    print(res)