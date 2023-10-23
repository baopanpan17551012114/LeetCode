"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = 1 if (dp[i-1][0] and obstacleGrid[i][0]!=1) else 0
        for j in range(1, n):
            dp[0][j] = 1 if (dp[0][j-1] and obstacleGrid[0][j]!=1) else 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]



if __name__ == '__main__':
    res = Solution().uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]])
    print(res)
