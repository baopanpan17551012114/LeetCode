#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你输⼊⼀个可包含重复数字的序列 nums，请你写⼀个算法，返回所有可能的全排列
⽐如输⼊ nums = [1,2,2]，函数返回：
[ [1,2,2],[2,1,2],[2,2,1] ]
"""
import copy
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        path_list = []
        used = [False] * len(nums)
        nums = sorted(nums)
        back_track(nums, result_list, path_list, used)
        return result_list


def back_track(nums, result_list, path_list, used):
    if len(path_list) == len(nums):
        result_list.append(copy.deepcopy(path_list))
        return
    for i in range(len(nums)):
        ele = nums[i]
        # 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
        if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
            continue  # 需要深刻理解为什么是continue，不是return
        # 该元素已经被使用过
        if used[i]:
            continue
        used[i] = True
        path_list.append(ele)
        back_track(nums, result_list, path_list, used)
        path_list.pop()
        used[i] = False


if __name__ == '__main__':
    nums = [1, 1, 2]
    res = Solution().permuteUnique(nums)
    print(res)
