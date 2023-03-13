#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
输⼊⼀个存储着整数的⼆维数组 grid，如果 grid[i][j] > 0，说明这个格⼦装着⾎瓶，经过它可以增加 对应的⽣命值；
如果 grid[i][j] == 0，则这是⼀个空格⼦，经过它不会发⽣任何事情；
如果 grid[i][j] < 0，说明这个格⼦有怪物，经过它会损失对应的⽣命值。
现在你是⼀名骑⼠，将会出现在最左上⻆，公主被困在最右下⻆，你只能向右和向下移动，请问你初始⾄少 需要多少⽣命值才能成功救出公主？
就是问你⾄少需要多少初始⽣命值，能够让骑⼠从最左上⻆移动到最右下⻆，且任何时候⽣命值 都要⼤于 0。
[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
7
"""
import numpy as np


def get_recursion(grid, i, j):
    # i, j表示从[i, j]位置到达右下角所需的最小生命值
    if i == len(grid)-1 and j == len(grid[0])-1:
        return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
    if i > len(grid)-1 or j > len(grid[0])-1:
        return np.Inf
    res = min(get_recursion(grid, i+1, j), get_recursion(grid, i, j+1)) - grid[i][j]
    return res if res > 0 else 1


def get_dp(grid):
    # dp[i][j]表示到达(i, j) (需要的最小生命值, 保留的生命值)
    dp = [[[0, 0] for j in range(len(grid[0]))] for i in range(len(grid))]
    # base case


if __name__ == '__main__':
    grid = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    # get_dp(grid)
    result = get_recursion(grid, 0, 0)
    print(result)