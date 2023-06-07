#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
注意：不允许旋转信封。


示例 1：
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: x[0])
        dp = [0 for i in range(len(envelopes))]
        dp[0] = 1
        for i in range(1, len(envelopes)):
            res = 1
            for j in range(i):
                if envelopes[i][0] <= envelopes[j][0] or envelopes[i][1] <= envelopes[j][1]:
                    continue
                else:
                    res = max(res, dp[j]+1)
            dp[i] = res

        return max(dp)


if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    res = Solution().maxEnvelopes(envelopes)
    print(res)
