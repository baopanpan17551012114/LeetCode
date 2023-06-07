#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你⼀个整数数组 nums，其中可能包含重复元素，请你返回该数组所有可能的⼦集。

⽐如输⼊ nums = [1,2,2]，应该输出：[[],[1],[2],[1,2],[2,2],[1,2,2]]
"""
import copy


def get_sub_sets_with_dup(nums):
    result_list = []
    path_list = []
    nums = sorted(nums)
    back_track(nums, result_list, path_list, 0)
    return result_list


def back_track(nums, result_list, path_list, index):
    result_list.append(copy.deepcopy(path_list))
    for i in range(index, len(nums)):
        # 剪枝，相同的数字，下一次不进入
        # if i > 0 and nums[i] == nums[i-1]:
        if i > index and nums[i] == nums[i-1]:  # index表示一个分支？
            continue
        path_list.append(nums[i])
        back_track(nums, result_list, path_list, i+1)
        path_list.pop()


if __name__ == '__main__':
    # nums = [1, 2, 2]
    nums = [10, 1, 2, 7, 6, 1, 5]
    res = get_sub_sets_with_dup(nums)
    print(res)