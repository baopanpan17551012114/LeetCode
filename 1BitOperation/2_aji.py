#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
一个数组中有一种数出现了奇数次，其他数都出现了偶数次，怎么找到并打印这种数
利用的就是位运算中 异或的基本性质
"""


def find_ji(arr: list):
    re = 0
    for ele in arr:
        re = re ^ ele
    return re


if __name__ == '__main__':
    arr = [1, 1, 2, 3, 3, 4, 4]
    re = find_ji(arr)
    print(re)
