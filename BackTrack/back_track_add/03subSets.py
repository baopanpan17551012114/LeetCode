#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
问题： 题⽬给你输⼊⼀个⽆重复元素的数组 nums，其中每个元素最多使⽤⼀次，请你返回 nums 的所有⼦集。

⽐如输⼊ nums = [1,2,3]，算法应该返回如下⼦集：
[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
"""
import copy


def get_subsets(nums):
    path_list = []
    result_list = []
    back_track(nums, path_list, result_list, 0)
    return result_list


def back_track(nums, path_list, result_list, index):
    # 结果保存
    if path_list not in result_list:
        result_list.append(copy.deepcopy(path_list))
    # 路径
    for i in range(index, len(nums)):
        path_list.append(nums[i])
        back_track(nums, path_list, result_list, i+1)
        path_list.pop()


if __name__ == '__main__':
    res = get_subsets([1, 2, 3])
    print(res)
