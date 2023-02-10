#!/usr/bin/env python
# -*- coding:utf-8 -*-
import copy

"""
题目描述：
给定一个不包含重复数字的数组，返回所有的数组的子集并且不能有重复。
"""


def get_sub_sets(num_list):
    result_list = []
    path_list = []
    back_track(num_list, result_list, path_list, 0)
    print(result_list)


def back_track(num_list, result_list, path_list, index):
    temp_list = copy.deepcopy(path_list)
    # 结果保存路径
    result_list.append(temp_list)
    for i in range(index, len(num_list)):  # i = 2
        path_list.append(num_list[i])  # [1, 2, 3]
        back_track(num_list, result_list, path_list, i+1)  # 3
        path_list.pop()
    # 一共四层，前三层有for循环
    # 保存[];
    # 第一层, i=0, [1], 1进入, 保存, 进入下一层(二);
    # 第二层, i=1, [1, 2], 2进入，保存, 进入下一层(三);
    # 第三层, i=2, [1, 2, 3], 3进入(四);
    # 第四层, 保存, i==3==len(num_list), for循环失效, 结束本层

    # 最深层(四)结束, [1, 2, 3]回退成[1, 2]; i=2, 次深层(三)for循环结束, 次深层结束;
    # [1, 2]回退成[1],
    # 第二层for后移, [1, 3], 3进入, 保存, 3==len(num_list), for循环失效, 次深层结束;
    # [1, 3]回退成[1], 最外层for第一个ele结束;
    # for第二个ele, [2], 2进入, 保存, 进入下一层; [2, 3], 3进入, 保存, 3==len(num_list), for循环失效;
    # for第三个ele


if __name__ == '__main__':
    get_sub_sets([1, 2, 3])