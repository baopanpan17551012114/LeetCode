#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
不用额外变量交换两个数的值

主要性质：
1、a ^ a  = 0
2、a ^ 0 = a
交换律，结合律
"""


def exchange(a, b):
    a = a ^ b
    b = a ^ b  # a^b^b = a
    a = a ^ b  # a^b^a = b
    return a, b


if __name__ == '__main__':
    a = 5
    b = 6
    a, b = exchange(a, b)
    print(a, b)
