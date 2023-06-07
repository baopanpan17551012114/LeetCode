#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你输⼊ candidates 和⼀个⽬标和 target，从 candidates 中找出中所有和为 target 的组合。
candidates 可能存在重复元素，且其中的每个数字最多只能使⽤⼀次。
说这是⼀个组合问题，其实换个问法就变成⼦集问题了：请你计算 candidates 中所有和为 target 的⼦集

输入: candidates =[10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
import copy
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res_list = []
        path_list = []
        candidates = sorted(candidates)
        back_track(res_list, path_list, 0, target, candidates)
        return res_list


def back_track(res_list, path_list, index, target, candidates):
    if sum(path_list) == target:
        res_list.append(copy.deepcopy(path_list))
        return

    if sum(path_list) > target:
        return

    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i-1]:
            continue
        path_list.append(candidates[i])
        back_track(res_list, path_list, i+1, target, candidates)
        path_list.pop()


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = Solution().combinationSum2(candidates, target)
    print(res)
