#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
输⼊⼀个字符串 ring 代表圆盘上的字符（指针位置在 12 点钟⽅向，初始指向 ring[0]），
再输⼊⼀个字符串 key 代表你需要拨动圆盘输⼊的字符串，
返回输⼊这个 key ⾄少进⾏多少次操作 （拨动⼀格圆盘和按下圆盘中间的按钮都算是⼀次操作）。
输⼊ ring = "godding", key = "gd"，返回： 4
"""
import numpy as np


def get_recursion(ring, i, key, j):
    # 递归
    # base case
    if j == len(key):
        return 0
    # 状态：ring[i]和key[j]; 选择：左旋转 还是 右旋转
    res = np.Inf
    for index in range(len(ring)):
        if key[j] == ring[index]:
            gap = abs(i - index)
            # 顺时针 还是 逆时针
            gap = min(gap, len(ring)-gap)
            child = get_recursion(ring, index, key, j+1)
            res = min(res, child + 1 + gap)
    return res


def get_dp(ring, key):
    # dp[i][j]表示在ring[i], key[j]时，需要执行的操作次数
    # base case
    dp = [[0 for j in range(len(key))] for i in range(len(ring))]


if __name__ == '__main__':
    ring = "godding"
    key = "gd"
    res = get_recursion(ring, 0, key, 0)
    print(res)

    get_dp(ring, key)
