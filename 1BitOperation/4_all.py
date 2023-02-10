#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1.&运算符:与运算符，两位都为1时，结果为1，否则为0。
2.|运算符:或运算符，两位都为0时，结果为0，否则为1。
3^运算符:异或运算符，两位相同时为0，不同为1。
4.~运算符:取反运算符，按位取反。
5.<<左移运算符:向左移动x位，数值大小变为原来的2x倍
取模，例如int型整数有32位，至多移32位，对于1<<35,1<<3结果是相同的。
6.>>右移运算符:向右移动x位，数值大小缩小为原来的2x倍
"""


def get_odd_even(value):
    """
    判断奇偶数
    :param value:
    :return:
    """
    result = value & 1
    if result == 1:
        return '奇数'
    else:
        return '偶数'


def get_find_twice(number_list):
    """
    1.找出唯一成对的数
    1-1000这1000个数放在含有1001个元素的数组中，只有唯一的一个元素值重复，其它均只出现一次。
    每一个数组元素只能访问一次，设计一个算法，将它找出来；不用辅助储存空间，能否设计一个算法实现？
    :param number_list:
    :return:
    """
    res = 0
    for i in range(1, len(number_list)):
        res = res ^ i
    for ele in number_list:
        res = res ^ ele
    print(res)


if __name__ == '__main__':
    re = get_find_twice([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10])