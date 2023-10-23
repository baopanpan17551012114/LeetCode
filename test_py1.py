"""
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def back_track(ele, left, right):
            print(ele)
            if left == n and right == n:
                result.append(ele)
            if left < n:
                ele += '('
                back_track(ele, left+1, right)
                ele = ele[0:-1]
            if left > right:
                ele += ')'
                back_track(ele, left, right + 1)
                ele = ele[0:-1]
        back_track('', 0, 0)
        return result


if __name__ == '__main__':
    # 回溯法
    pass