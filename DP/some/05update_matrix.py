"""
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
"""
import copy
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        matrix = [[-1 for j in range(n)] for i in range(m)]
        sign_matrix = copy.deepcopy(matrix)
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j])
                    sign_matrix[i][j] = 1
                    matrix[i][j] = 0
        while q:
            tmp_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            ele = q.pop(0)
            for tmp in tmp_list:
                index_x = ele[0]+tmp[0]
                index_y = ele[1]+tmp[1]
                if index_x < 0 or index_y < 0 or index_x >= m or index_y >= n or sign_matrix[index_x][index_y] == 1:
                    continue
                matrix[index_x][index_y] = matrix[ele[0]][ele[1]] + 1
                q.append([index_x, index_y])
        return matrix



if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    res = Solution().updateMatrix(mat)
    print(res)