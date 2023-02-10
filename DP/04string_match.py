#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
exp中的'.'代表任何一个字符，B中的'*'表示'*'的前一个字符可以有0个或者多个。请写一个函数，判断A是否能被B匹配。
给定两个字符串A和B,同时给定两个串的长度lena和lenb，请返回一个bool值代表能否匹配。保证两串的长度均小于等于300。

测试样例：
“abcd”,4,”.*”,2
返回：true
"""


def get_string_match(str1, length1, str2, length2):
    if str2[0] != '.' and str2[0] != str1[0]:
        return 0
    dp = [[0 for i in range(length2)] for j in range(length1)]
    for i in range(length1):
        for j in range(length2):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0 or j == 0:
                continue
            else:
                if str2[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif str2[j] == '*':
                    pass
                else:
                    dp[i][j] = dp[i-1][j-1] and str1[i-1] == str2[j-1]