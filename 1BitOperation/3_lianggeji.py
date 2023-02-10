#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
一个数组中有两种数出现了奇数次，其他数都出现了偶数次，怎么找到并打印这两种数
思路：
对数组中所有数做异或操作后，value = a ^ b
两个数不同，则value != 0，即value中至少有一个二进制位不为0
任意一个value中不为0的二进制位，数组中其它数字在该位0和1都出现了偶数次，a和b在该位分别为0和1
所以，挑选那些数字在该位为0或1做异或，就得到a或者b中一个
"""


def right_one(a):
    # 获取最右侧不为0的二进制位
    return ~a + 1


def find_2_ji(arr: list):
    re = 0
    for ele in arr:
        re = re ^ ele  # re = a ^ b

    a = 0
    for ele in arr:
        # 指定位为0/1
        if right_one(re) & ele == 0:
            a = a ^ ele
    b = re ^ a
    return a, b


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 4, 4]
    a, b = find_2_ji(arr)
    print(a, b)

