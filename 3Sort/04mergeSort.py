#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""基础归并排序
master公式和时间复杂度
T(N) = a * (T / b) + O(T**d)
"""


def merge_sort(list_left, list_right):
    """"""
    list_extra = []
    i = 0
    j = 0
    while i < len(list_left) and j < len(list_right):
        if list_left[i] <= list_right[j]:
            list_extra.append(list_left[i])
            i += 1
        else:
            list_extra.append(list_right[j])
            j += 1
    if i < len(list_left):
        for ele in list_left[i:]:
            list_extra.append(ele)
    if j < len(list_right):
        for ele in list_right[j:]:
            list_extra.append(ele)
    return list_extra


def process(arr: list):
    """"""
    if len(arr) == 1:
        return arr

    mid = int(len(arr) / 2)
    left_list = process(arr[0:mid])
    right_list = process(arr[mid:])

    return merge_sort(left_list, right_list)


if __name__ == '__main__':
    arr = [2, 3, 5, 4, 1, 7, 6]
    re = process(arr)
    print(re)

