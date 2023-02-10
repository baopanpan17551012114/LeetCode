#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目描述：
给定一个含有重复数字的数组，返回所有的数组的子集并且不能有重复

这道题是在上一题的基础上做了一点改变就是数组中含有重复的数字，我们在遍历的过程中要想办法来消除掉重复，那么如何才能做到呢？
其实很简单，首先我们对整个数组进行排序，这样重复的数字就会靠在一起，然后我们在构建多叉树的时候对于重复的数字只用一次即可。
如例子中有两个2，那么根节点下面的子节点就只有一个2。按照这种思路例子中的数组可以构建成如下所示的多叉树
"""
import copy


def get_sub_sets(num_list):
    result_list = []
    path_list = []
    num_list = sorted(num_list)
    back_track(num_list, result_list, path_list, 0)
    print(result_list)


def back_track(num_list, result_list, path_list, index):
    temp_list = copy.deepcopy(path_list)
    # 结果保存路径
    result_list.append(temp_list)
    for i in range(index, len(num_list)):
        # if num_list[i] == num_list[i-1]:
        #     print(index, i)
        if i > index and num_list[i] == num_list[i-1]:
            continue
        path_list.append(num_list[i])
        back_track(num_list, result_list, path_list, i+1)
        path_list.pop()


if __name__ == '__main__':
    get_sub_sets([1, 2, 2])
