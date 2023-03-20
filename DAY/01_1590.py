#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
子数组 定义为原数组中连续的一组元素。

示例 1：
输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。

示例 2：
输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。

示例 3：
输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。

示例  4：
输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。

示例 5：
输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0
"""
from typing import List

import numpy as np


def minSubarray(nums: List[int], p: int) -> int:
    x = sum(nums) % p
    if x == 0: return 0  # 移除空子数组（这行可以不要）

    ans = n = len(nums)
    s = 0
    last = {s: -1}  # 由于下面 i 是从 0 开始的，前缀和下标就要从 -1 开始了
    for i, v in enumerate(nums):
        s += v
        last[s % p] = i
        j = last.get((s - x) % p, -n)  # 如果不存在，-n 可以保证 i-j >= n
        ans = min(ans, i - j)  # 改成手写 min 会再快一些
    return ans if ans < n else -1


"""
首先，我们要知道一个数学性质：
如果两个数的差能被 p 整除，那么它们对 p 取模的结果相等。比如 10 - 4 = 6 能被 3 整除，那么 10 % 3 = 1 和 4 % 3 = 1 也相等
"""


def get_min_array(nums, p):
    x = sum(nums)
    mod = sum(nums) % p
    if mod == 0:
        return 0
    # 前缀和
    sum_arr = [0]
    for i, v in enumerate(nums):
        sum_arr.append(sum_arr[-1] + v)

    # 求余
    mod_dict = {}
    length = len(nums)
    for i in range(len(nums)):
        s = sum_arr[i+1]
        key = (s - x) % p
        j = mod_dict.get(key, -np.Inf)
        length = min(length, i-j)

        mod_i = s % p
        mod_dict[mod_i] = i  # 保存余数及对应位置
    return length if length < len(nums) else -1


if __name__ == '__main__':
    nums = [1,2,3]
    p = 3
    res = get_min_array(nums, p)
    print(res)

    res = minSubarray(nums, p)
    print(res)
