#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
输⼊⼀个⼆维矩阵，0 表示海⽔，1 表示陆地，计算 不同的 (distinct) 岛屿数量
"""
from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res_list = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    diff_list = list()
                    dfs(grid, i, j, 0, diff_list)
                    diff_str = ','.join(diff_list)
                    if diff_str not in res_list:
                        diff_list.append(diff_str)
        return len(res_list)


def dfs(grid, i, j, value, diff_list):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    if grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    diff_list.append(value)
    dfs(grid, i + 1, j, 1, diff_list)
    dfs(grid, i - 1, j, 2, diff_list)
    dfs(grid, i, j + 1, 3, diff_list)
    dfs(grid, i, j - 1, 4, diff_list)
    diff_list.append(-value)


if __name__ == '__main__':
    pass
