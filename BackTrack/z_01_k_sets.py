#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
"""
import copy


def get_k_sets(n, k):
    path_list = []
    result_list = []
    back_track(result_list, path_list, k, n)
    print(result_list)


def back_track(result_list, path_list, k, n):
    # 组合长度==k，符合要求，保存
    if len(path_list) == k:
        result_list.append(copy.deepcopy(path_list))
    for i in range(1, n):
        # 当前数字在组合中已存在，则跳过
        if i in path_list:
            continue
        path_list.append(i)
        back_track(result_list, path_list, k, n)
        path_list.pop()


if __name__ == '__main__':
    get_k_sets(4, 2)
