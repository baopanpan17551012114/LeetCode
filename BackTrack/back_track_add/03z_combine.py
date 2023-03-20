#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
「组合」： 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

⽐如 combine(3, 2) 的返回值应该是：
[[1,2],[1,3],[2,3]]
"""
import copy


def get_combine(n, k):
    nums = [i+1 for i in range(n)]
    path_list = []
    result_list = []
    back_track(nums, path_list, result_list, 0, k)
    return result_list


def back_track(nums, path_list, result_list, index, k):
    # 结果保存
    if len(path_list) == k:
        result_list.append(copy.deepcopy(path_list))
    for i in range(index, len(nums)):
        path_list.append(nums[i])
        back_track(nums, path_list, result_list, i+1, k)
        path_list.pop()


if __name__ == '__main__':
    res = get_combine(3, 2)
    print(res)
