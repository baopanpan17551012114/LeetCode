#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目描述： 给定一个不包含重复的数组，返回所有可能的排列
"""
import copy


def get_permutation(num_list):
    result_list = []
    path_list = []
    back_track(num_list, result_list, path_list)
    print(result_list)


def back_track(num_list, result_list, path_list):
    if len(path_list) == len(num_list):
        tmp_path_list = copy.deepcopy(path_list)
        result_list.append(tmp_path_list)
    else:
        for i in range(0, len(num_list)):
            # 不重复数组，所以子节点不能和父节点值一样; 本质是为了不让相同index的节点进入path_list两次
            if num_list[i] in path_list:
                continue
            path_list.append(num_list[i])
            back_track(num_list, result_list, path_list)
            path_list.pop()


if __name__ == '__main__':
    get_permutation([1, 2, 3])