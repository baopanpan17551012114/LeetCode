#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你⼀个⽆重复元素的整数数组 candidates 和⼀个⽬标和 target，找出 candidates 中可以使数字和 为⽬标数 target 的所有组合。
candidates 中的每个数字可以⽆限制重复被选取。
⽐如输⼊ candidates = [1,2,3], target = 3，算法应该返回：
[ [1,1,1],[1,2],[3] ]
"""
import copy
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []
        path_list = []
        back_track(candidates, target, result_list, path_list, 0)
        return result_list


def back_track(candidates, target, result_list, path_list, index):
    if sum(path_list) == target:
        result_list.append(copy.deepcopy(path_list))
        return

    if sum(path_list) > target:
        return

    for i in range(index, len(candidates)):  # 组合问题因为不考虑顺序，所以一定要index来保证不重复
        ele = candidates[i]
        path_list.append(ele)
        back_track(candidates, target, result_list, path_list, i)
        path_list.pop()


if __name__ == '__main__':
    candidates = [1, 2, 3]
    target = 3
    res = Solution().combinationSum(candidates, target)
    print(res)