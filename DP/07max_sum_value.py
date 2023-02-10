#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
最大连续子序列和
对于一个有正有负的整数数组，请找出总和最大的连续数列。
测试样例：
[1,2,3,-6,1]
返回：6

输出最大连续子序列
最大连续子序列是所有连续子序列中元素和最大的一个，
例如给定序列{ -2, 11, -4, 13, -5, -2 }，其最大连续子序列为{ 11, -4, 13 }，最大和为20。
现在增加一个要求，即还需要输出该子序列的第一个和最后一个元素。

最长递增子序列LIS
题目描述：
给定一个长度为N的数组，找出一个最长的单调自增子序列（不一定连续，但是顺序不能乱）。
例如：给定一个长度为6的数组A{5， 6， 7， 1， 2， 8}，则其最长的单调递增子序列为{5，6，7，8}，长度为4.
假设存在一个序列d[1..9] ={ 2，1 ，5 ，3 ，6，4， 8 ，9， 7}，可以看出来它的LIS长度为5。\

5.1最大连续子序列乘积
题目描述
输入n个元素组成的序列S，你需要找出一个乘积最大的连续子序列，如果这个最大乘积不是正数，则输出0。
输入输入n个整数表示序列的元素
（-10<=元素<=10）以空格分隔，最后一个数字之后无空格）。
样例输入
2 4 -3
样例输出
8
"""


def get_max_sum_value(value_list):
    dp = [0 for i in range(len(value_list))]
    dp[0] = value_list[0]
    # dp[i-1]表示包含A[i-1]时最大序列和
    for i in range(1, len(value_list)):
        dp[i] = max(dp[i-1]+value_list[i], value_list[i])
    print(dp)


def get_max_sum_value_beta(value_list):
    sum_value = 0
    result_value = 0
    for i in range(len(value_list)):
        sum_value += value_list[i]
        if sum_value <= 0:
            sum_value = 0
            continue
        else:
            if result_value < sum_value:
                result_value = sum_value
    print(result_value)


def get_max_sum_sequence(value_list):
    """最大连续子序列"""
    dp = [0 for i in range(len(value_list))]
    dp[0] = value_list[0]
    start_index = 0
    end_index = 1
    index_list = [[0, 1]]
    # dp[i-1]表示包含A[i-1]时最大序列和
    for i in range(1, len(value_list)):
        dp[i] = max(dp[i-1]+value_list[i], value_list[i])
        if dp[i] == value_list[i]:
            start_index = i
            end_index = i+1
        else:
            end_index = i+1
        index_list.append([start_index, end_index])
    print(dp)
    print(index_list)
    print(value_list[start_index: end_index])


def get_lis(value_list):
    # dp[i] = dp[i-1]
    pass


def get_max_product(value_list):
    # 同时记录最大和最小乘积
    dp_max = [0 for i in range(len(value_list))]
    dp_min = [0 for i in range(len(value_list))]
    dp_max[0] = value_list[0]
    dp_min[0] = value_list[0]

    for i in range(1, len(value_list)):
        dp_max[i] = max(dp_max[i - 1]*value_list[i], dp_min[i-1]*value_list[i], value_list[i])
        dp_min[i] = min(dp_max[i - 1] * value_list[i], dp_min[i - 1] * value_list[i], value_list[i])
    print(dp_max)
    print(dp_min)


if __name__ == '__main__':
    get_max_sum_value([1, 2, 3, -6, 1])
    get_max_sum_value_beta([1, 4, -3, 6, 1])

    get_max_sum_sequence([1, 2, 3, -6, 1])

    get_max_product([2, 4, -3, -6])