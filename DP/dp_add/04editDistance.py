#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
编辑距离
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成

eg: word1='horse', word2='ros' res=3
    word1='intention', word2='execution' res=5
"""


def get_recursion(word1, word2):
    # base case
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    # 状态转移
    length1 = len(word1)
    length2 = len(word2)
    # 最后一位相同时
    if word1[length1-1] == word2[length2-1]:
        return get_recursion(word1[:length1 - 1], word2[:length2 - 1])
    return (min(
        get_recursion(word1[:length1 - 1], word2[: length2 - 1]),  # 替换
        get_recursion(word1[:length1 - 1], word2[: length2]),  # 删除
        get_recursion(word1[:length1], word2[: length2 - 1])  # 插入
    ) + 1)


def get_dp(word1, word2):
    length1 = len(word1)
    length2 = len(word2)
    dp = [[0 for i in range(length2+1)] for j in range(length1+1)]
    # base case
    for i in range(1, length1+1):
        dp[i][0] = i
    for i in range(1, length2+1):
        dp[0][i] = i
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if word1[i-1] == word2[j-1]:
                tmp_v1 = dp[i-1][j-1]
            else:
                tmp_v1 = dp[i-1][j-1] + 1
            dp[i][j] = min(tmp_v1, dp[i][j-1]+1, dp[i-1][j]+1)
    return dp[-1][-1]


if __name__ == '__main__':
    # 递归
    result = get_recursion(word1='horse', word2='ros')
    print(result)
    result = get_recursion(word1='intention', word2='execution')
    print(result)

    # 动态规划
    result = get_dp(word1='horse', word2='ros')
    print(result)
    result = get_dp(word1='intention', word2='execution')
    print(result)
