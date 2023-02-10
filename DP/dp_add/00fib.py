#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""斐波拉契数列"""


# 递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


# dp
def fib_dp(n):
    if n == 1 or n == 2:
        return 1
    value_n_2 = 1
    value_n_1 = 1
    value = 0
    for i in range(3, n+1):
        value = value_n_2 + value_n_1
        value_n_2 = value_n_1
        value_n_1 = value
    return value


if __name__ == '__main__':
    re = fib(6)
    print(re)
    re = fib_dp(6)
    print(re)
