"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。

示例 1:
输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
"""
import math


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        if n == 3:
            return 2
        v1 = self.get_number(n, 2)
        for k in range(3, n):
            v2 = self.get_number(n, k)
            if v1 < v2:
                v1 = v2
            else:
                break
        return v1

    def get_number(self, n, k):
        base_value = int(n / k)
        value_list = [base_value] * k
        for i in range(n-base_value*k):
            value_list[i] += 1
        total_value = 1
        for ele in value_list:
            total_value *= ele
        return total_value

if __name__ == '__main__':
    n = 11
    res = Solution().integerBreak(n)
    print(res)