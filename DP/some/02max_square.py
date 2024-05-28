"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1 if matrix[0][0] == '1' else 0

        max_value = dp[0][0]
        for i in range(1, m):
            dp[i][0] = matrix[i][0] == '1'
            max_value = max(dp[i][0], max_value)
        for j in range(1, n):
            dp[0][j] = matrix[0][j] == '1'
            max_value = max(dp[0][j], max_value)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
                max_value = max(max_value, dp[i][j])
        return max_value * max_value


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    res = Solution().maximalSquare(matrix)
    print(res)