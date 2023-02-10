#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
全排列问题
[1, 2, 3]
"""
import copy


def permute():
    result = []
    backtrack([], [1, 2, 3], result)
    print(result)


def backtrack(num_list, path_list, result):
    # 触发结束条件
    if len(path_list) == len(num_list):
        result.append(num_list)
        return
    for ele in path_list:
        # 排除不合法的选择
        if ele in num_list:
            continue
        # 选择
        num_list.append(ele)
        # 进入下一层决策树
        backtrack(copy.deepcopy(num_list), path_list, result)
        # 撤销选择
        num_list.remove(ele)


if __name__ == '__main__':
    permute()