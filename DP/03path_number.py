#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
有一个X*Y的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，计算机器人有多少种走法。
给定两个正整数int x,int y，请返回机器人的走法数目。保证x＋y小于等于12。
测试样例：
2,2
返回：2


变种：机器人障碍走方格
题目描述
有一个X*Y的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。
请设计一个算法，计算机器人有多少种走法。注意这次的网格中有些障碍点是不能走的。

给定一个int[][],表示网格图，若map[i][j]为1则说明该点不是障碍点，
否则则为障碍。另外给定int x,int y，表示网格的大小。请返回机器人从(0,0)走到(x - 1,y - 1)的走法数
"""


def get_path_number(x, y):
    matrix_value = [[1 for i in range(y)] for j in range(x)]
    for i in range(x):
        for j in range(y):
            if i == 0 or y == 0:
                continue
            else:
                matrix_value[i][j] = matrix_value[i-1][j] + matrix_value[i][j-1]
    print(matrix_value)


def get_path_number_alpha(matrix_value, x, y):
    for i in range(x):
        for j in range(y):
            if i == 0 and j == 0:
                continue
            if i == 0 and j != 0:
                matrix_value[i][j] = 0 if matrix_value[i][j-1] == 0 else 1
            elif i != 0 and j == 0:
                matrix_value[i][j] = 0 if matrix_value[i-1][j] == 0 else 1
            else:
                matrix_value[i][j] = matrix_value[i-1][j] + matrix_value[i][j-1] if matrix_value[i][j] != 0 else 0
    print(matrix_value)


if __name__ == '__main__':
    get_path_number_alpha()