#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
要求我们实现⼀个简单的正则匹配算法，包括「.」通配符和「*」通配符。
这两个通配符是最常⽤的，其中点号「.」可以匹配任意⼀个字符，星号「*」可以让之前的那个字符重复任意次数（包括 0 次）。
⽐如说模式串 ".a*b" 就可以匹配⽂本 "zaaab"，也可以匹配 "cb"；
模式串 "a..b" 可以匹配⽂本"amnb"；
⽽模式串 ".*" 就⽐较⽜逼了，它可以匹配任何⽂本。
题⽬会给我们输⼊两个字符串 s 和 p，s 代表⽂本，p 代表模式串，请你判断模式串 p 是否可以匹配⽂本 s。
我们可以假设模式串只包含⼩写字⺟和上述两种通配符且⼀定合法，不会出现 *a 或者 b** 这种不合法的模式串，
"""


def get_dp(s, p):
    """
    dp[i]表示以s[i] 和 p[i]结尾能否匹配
    :param s:
    :param p:
    :return:
    """
    # 能匹配表示最终两个字符串长度相等
    j = 0
    tmp = p[0]
    for i in range(len(s)):
        print(i, s[i], tmp, j)
        if p[j] != '*':
            if tmp == s[i] or tmp == '.':
                j += 1
                if p[j] != '*':
                    tmp = p[j]
            else:
                return False

        elif p[j] == '*':  # 不匹配，但是为*
            # 前一位字符匹配，指针不变，tmp字符不变
            if tmp == s[i]:
                continue
            # 前一位不匹配，但是后一位匹配
            elif p[j+1] == s[i] or p[j+1] == '.':
                tmp = p[j + 1]
                j += 2
            else:
                return False
        else:
            return False

    return True


if __name__ == '__main__':
    result = get_dp("cb", ".a*b")
    print(result)