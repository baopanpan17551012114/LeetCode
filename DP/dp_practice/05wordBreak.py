#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
"""
from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        L = len(s)
        @cache
        def back_track(i):
            if i == L:
                return True
            for j in range(i+1, L+1):
                if s[i:j] in wordDict and back_track(j):
                    return True
            return False
        return back_track(0)


if __name__ == '__main__':
    s = "ccbb"
    wordDict = ["bc", "cb"]
    res = Solution().wordBreak(s, wordDict)
    print(res)


