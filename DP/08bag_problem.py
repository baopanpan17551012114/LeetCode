#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
题目描述：
有n个物品，它们有各自的体积和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和
eg：number＝4，capacity＝5
w:[2, 1, 3, 2]
v:[3, 2, 4, 2]

利用动态规划来解决,每次遍历到的第 i 个物品，根据 weight[i] 与 value[i] 来确定是否需要将该物品放入背包中。即对于给定的 n个物品，
设 weight[i]、value[i] 分别为第 i 个物品的重量与价值，m 为背包的容量。
再令 v[i][j] 表示在前 i 个物品中进行组合后装入容量为 j 的背包中的最大价值。则有下面的结果：
(1) v[0][i] = v[i][0]=0; // 表示 填入表 第一行和第一列都是 0
(2) 当 weight[i] > j 时，v[i][j] = v[i-1][j]; // 当准备加入的新增的商品的重量大于当前背包的容量时，就直接使用上一个单元格的装入策略
(3) 当 j >= weight[i-1] 时： v[i][j]=max{v[i-1][j], value[i] + v[i-1][j-weight[i]]} // 当准备加入的新增的商品的重量小于或者等于当前背包的容量时,使用的装入策略，
各部分说明如下
v[i-1][j]： 就是上一个单元格的装入的最大价值
value[i] : 表示当前商品的价值
v[i-1][j-weight[i]] ： 装入前 i-1 个商品，到剩余背包容量 j-weight[i] 的最大价值
当 j >= weight[i] 时： v[i][j] = max{v[i-1][j], value[i]+v[i-1][j-weight[i]]} ;
"""


def get_max_bag_value(w, v, capacity):
    #
    dp = [[0 for i in range(capacity+1)] for j in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, capacity+1):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
    print(dp)
    print(dp[-1][-1])


if __name__ == '__main__':
    get_max_bag_value([1, 2, 3], [40, 30, 10], 4)










