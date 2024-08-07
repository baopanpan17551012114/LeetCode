#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你两个单词word1 和word2， 请返回将word1转换成word2 所使用的最少操作数。

你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符


示例1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        # base case
        dp[0][0] = 0
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for j in range(1, len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "horse"
    res = Solution().minDistance(word1, word2)
    print(res)