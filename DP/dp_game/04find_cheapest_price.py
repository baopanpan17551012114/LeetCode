#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题⽬会给你输⼊若⼲参数：
正整数 n 代表城市个数，数组 flights 装着若⼲三元组代表城市间的航线及价格，城市编号 src 代表你所在的城市，城市编号 dst 代表你要去的⽬标城市，
整数 K 代表你最多经过的中转站个数。
请你的算法计算，在 K 次中转之内，从 src 到 dst 所需的最⼩花费是多少钱，如果⽆法到达，则返回 -1。 ⽐⽅说题⽬给的例⼦：
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1, 返回值应该是 200。
k = 0, 500
"""
import numpy as np


def get_recursion(s, k, dst, flights):
    # base case
    if s == dst:
        return 0
    if k == 0:
        return -1
    # 状态：当前城市 和 剩余中转
    # 选择：下一步可抵达城市
    res = np.Inf
    for ele in flights:
        s1, d1, w1 = ele
        if s1 == s:
            child = get_recursion(d1, k-1, dst, flights)
            if child != -1:
                res = min(res, child + w1)
    return res if res != np.Inf else -1


if __name__ == '__main__':
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    k = 0
    res = get_recursion(0, k + 1, 2, flights)
    print(res)