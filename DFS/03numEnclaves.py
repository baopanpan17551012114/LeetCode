#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。

输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
"""
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 先要将靠边的0变成1
        for i in range(0, len(grid)):
            dfs(grid, i, 0)
            dfs(grid, i, len(grid[0])-1)
        for j in range(0, len(grid[0])):
            dfs(grid, 0, j)
            dfs(grid, len(grid)-1, j)
        total_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_num += 1  # 是网格数量，不是岛屿数量，所以不用淹没
                    # dfs(grid, i, j)
        return total_num


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return
    if grid[i][j] == 0:
        return

    grid[i][j] = 0
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


if __name__ == '__main__':
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    result = Solution().numEnclaves(grid)
    print(result)