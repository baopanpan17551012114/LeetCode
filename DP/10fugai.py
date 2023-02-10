#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目描述
可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


def get_total_type(number):
    dp = [0 for i in range(number+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, number+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)


"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


def get_total_type_alpha(number):
    # f(n) = f(n-1) + f(n-2)
    if number < 2:
        return number
    a = 0
    b = 1
    c = 0
    for i in range(2, number+1):
        c = a + b
        a = b
        b = c
    print(c)