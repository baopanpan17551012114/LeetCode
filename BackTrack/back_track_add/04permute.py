#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
排列问题： 给定⼀个不含重复数字的数组 nums，返回其所有可能的全排列。

⽐如输⼊ nums = [1,2,3]，函数的返回值应该是： [
 [1,2,3],[1,3,2],
 [2,1,3],[2,3,1],
 [3,1,2],[3,2,1] ]
"""
import copy


def get_permute(nums):
    path_list = []
    result_list = []
    back_track(nums, result_list, path_list)
    return result_list


def back_track(nums, result_list, path_list):
    # 结果保存
    if len(path_list) == len(nums):
        result_list.append(copy.deepcopy(path_list))
        return

    for ele in nums:
        # 排除不合法的选择
        if ele in path_list:
            continue
        path_list.append(ele)
        back_track(nums, result_list, path_list)
        path_list.pop()


if __name__ == '__main__':
    res = get_permute([1, 2, 3])
    print(res)
