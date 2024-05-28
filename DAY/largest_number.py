"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"
"""
from typing import List

from functools import cmp_to_key
class Solution:
    def compare(self, x, y):
        if x + y > y + x:
            return 1
        return -1

    def largestNumber(self, nums: List[int]) -> str:
        # 优先最高位的数排序(个位数对应最大数), 然后是降一位
        str_number_list = [str(num) for num in nums]
        str_number_list.sort(key=cmp_to_key(self.compare), reverse=True)
        res = ''.join(str_number_list)
        if res[0] == '0':
            return '0'
        return ''.join(str_number_list)

if __name__ == '__main__':
    Solution().largestNumber([3,30,34,5,9])