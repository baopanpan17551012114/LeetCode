#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""路径经过的最大值（最小值）：
题目描述：平面上有N*M个格子，每个格子中放着一定数量的苹果。
从左上角的格子开始， 每一步只能向下走或是向右走，每次走到一个格子就把格子里的苹果收集起来， 这样一直走到右下角，问最多能收集到多少个苹果。"""


def get_max_value(matrix_value):
    """max(n*m) = max((n-1)*m+a, max(n*(m-1))+b)"""
    m = len(matrix_value)
    n = len(matrix_value[0])
    # 存放中间结果的矩阵
    for i in range(m):
        for j in range(n):
            if j == 0 and i == 0:
                matrix_value[i][j] = matrix_value[i][j]
            elif j == 0 and i != 0:
                matrix_value[i][j] += matrix_value[i - 1][j]
            elif j != 0 and i == 0:
                matrix_value[i][j] += matrix_value[i][j-1]
            else:
                matrix_value[i][j] += max(matrix_value[i-1][j], matrix_value[i][j-1])
    print(matrix_value)


if __name__ == '__main__':
    get_max_value()