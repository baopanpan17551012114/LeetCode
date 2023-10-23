#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。

每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。


示例 1：

输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if grid[0][0] == -1:
            return 0
        m = len(grid)
        n = len(grid[0])
        def dfs(x, y, left):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0:
                return 0
            if grid[x][y] == 2:
                return left == 0
            grid[x][y] = -1
            ans = dfs(x-1, y, left-1) + dfs(x+1, y, left-1) + dfs(x, y-1, left-1) + dfs(x, y+1, left-1)
            grid[x][y] = 0
            return ans
        left = sum(row.count(0) for row in grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j, left+1)






if __name__ == '__main__':
    res = Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(res)