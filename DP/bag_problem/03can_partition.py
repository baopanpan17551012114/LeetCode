#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
输⼊⼀个只包含正整数的⾮空数组 nums，请你写⼀个算法，判断这个数组是否可以被分割成两个⼦集，使得 两个⼦集的元素和相等。
⽐如说输⼊ nums = [1,5,11,5]，算法返回 true，因为 nums 可以分割成 [1,5,5] 和 [11] 这两个⼦ 集。
如果说输⼊ nums = [1,3,2,5]，算法返回 false，因为 nums ⽆论如何都不能分割成两个和相等的⼦集。
"""

def get_dp(nums):
    """
    问题等价于：total/2, 每个数字只能放一次，能否正好凑成
    :param nums:
    :return:
    """
    # 选择：放 或者 不放
    # 状态：total 和 num
    if sum(nums) % 2 == 1:
        print(0)
        return
    total = int(sum(nums) / 2)
    dp = [[0 for j in range(total+1)] for i in range(len(nums)+1)]
    # base case:
    for i in range(len(nums)+1):
        dp[i][0] = 1
    for i in range(1, len(nums)+1):
        for j in range(1, total+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]] if j-nums[i-1] >= 0 else 0)
    print(dp[-1][-1])


if __name__ == '__main__':
    get_dp([1, 5, 11, 5])
