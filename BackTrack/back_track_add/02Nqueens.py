#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你⼀个 N×N 的棋盘，让你放置N个皇后，使得它们不能互相攻击。 PS：皇后可以攻击同⼀⾏、同⼀列、左上左下右上右下四个⽅向的任意单位。
"""
import copy


def get_n_queen(n):
    result = []
    child_result = []
    for i in range(n):
        child_result.append([0]*n)
    back_track(child_result, 0, result)
    print(result)


def back_track(child_result, n, result):
    # 终止条件
    if n == len(child_result):
        result.append(child_result)
        return

    # 路径选择
    for i in range(len(child_result)):
        # 非法选择
        if is_illegal(child_result, n, i):
            continue
        child_result[n][i] = 1

        # 进入下一层决策树
        back_track(copy.deepcopy(child_result), n+1, result)
        # 撤销选择
        child_result[n][i] = 0


def is_illegal(child_result, i, j):
    # 横向
    for ele in child_result[i]:
        if ele == 1:
            return 1
    # 纵向
    for n in range(len(child_result)):
        if child_result[n][j] == 1:
            return 1
    # 斜向
    n = min(j, i)
    for m in range(1, n+1):
        if child_result[i-m][j-m] == 1:
            return 1
    n = min(len(child_result)-i, len(child_result)-j)
    for m in range(1, n):
        if child_result[i+m][j+m] == 1:
            return 1
    return 0


if __name__ == '__main__':
    get_n_queen(4)
