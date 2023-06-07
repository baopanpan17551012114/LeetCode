#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
封闭岛屿的数量
1、⽤ 0 表示陆地，⽤ 1 表示海⽔。
2、让你计算「封闭岛屿」的数⽬。所谓「封闭岛屿」就是上下左右全部被 1 包围的 0，也就是说靠边的陆地 不算作「封闭岛屿」。

输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
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
                if grid[i][j] == 0:
                    total_num += 1
                    dfs(grid, i, j)
        return total_num


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return
    if grid[i][j] == 1:
        return

    grid[i][j] = 1
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    result = Solution().closedIsland(grid)
    print(result)