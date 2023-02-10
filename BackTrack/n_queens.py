#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
n皇后问题，将n替换成8就是经典的8皇后问题。
在国际象棋中，皇后可以沿着竖排、横排、双向对角线进行攻击，题目要求给定一个整数n, 在一个n * n的棋盘上放置n个皇后，
并且这些皇后彼此之间都攻击不到对方，返回所有可能的结果

之前的题目都是遍历一个一维的数组，这个题目遍历的是一个二维数组，我们还是可以一样应用回溯法来解决。
我们可以从第一行开始尝试每个位置，当我们在第一行中放置一个皇后后，当前行肯定不能再插入了，就需要在下一行中找到一个合法的位置放置下一个皇后。
而为了判断某个位置是否能够放置皇后，我们还需要创建一个 n * n 大小的二维数组来记录已经放入皇后的位置。这样当我们放置了n个皇后后就找到了一个解
"""
import copy


def get_solve_n_queens(n):
    result = []
    path = [[0 for i in range(n)] for j in range(n)]
    back_track(result, path, 0, n)
    print(result)


def back_track(result, path, row, n):
    # 当每行都摆了皇后时，产生一种解法
    if row == n:
        result.append(copy.deepcopy(path))
    # 一行一行地摆放，在确定一行中的那个皇后应该摆在哪一列时，需要当前列是否合法。
    # 如果合法，则将皇后放置在当前位置，并进行递归，回溯。
    for i in range(n):
        # 第row行在第i列是合法第
        if is_valid(path, row, i, n):
            path[row][i] = 1
            # 递归，进入下一行
            back_track(result, path, row+1, n)
            # 回溯
            path[row][i] = 0


def is_valid(path, row, column, n):
    # 向上检查竖排
    for i in range(row-1, -1, -1):
        if path[i][column]:
            return False
    # 左上对角线
    for i in range(1, row+1):
        if row-i < 0 or column-i < 0:
            break
        if path[row-i][column-i]:
            return False
    # 右上对角线
    for i in range(1, row+1):
        if row-i < 0 or column+i > n-1:
            break
        if path[row-i][column+i]:
            return False
    return True


if __name__ == '__main__':
    get_solve_n_queens(5)