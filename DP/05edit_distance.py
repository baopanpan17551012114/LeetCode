#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
最小编辑距离
"""


def get_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    print(dp)


# def min_edit_distance(a, b):
#     dp = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
#     for i in range(len(a) + 1):
#         dp[i][0] = i
#     for j in range(len(b) + 1):
#         dp[0][j] = j
#     for i in range(1, len(a) + 1):
#         for j in range(1, len(b) + 1):
#             if a[i - 1] == b[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
#     print(dp[-1][-1])


if __name__ == '__main__':
    get_edit_distance('abc', 'adc')
    # min_edit_distance('abc', 'adc')