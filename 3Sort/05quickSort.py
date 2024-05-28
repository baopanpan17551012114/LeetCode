#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
递归和非递归实现快排
"""

# def quick_sort(arr, left, right):
#     value = arr[left]  # 哨兵值
#     while left < right:
#         while left < right and arr[right] > value:
#             right -= 1
#         arr[left] = arr[right]
#         while left < right and arr[left] < value:
#             left += 1
#         arr[right] = arr[left]
#     arr[left] = value
#     return left
import sys


def quick_sort(array, start, end):
    if start >= end:
        return
    mid_data, left, right = array[start], start, end
    while left < right:
        while array[right] >= mid_data and left < right:
            right -= 1
        array[left], array[right] = array[right], array[left]
        while array[left] <= mid_data and left < right:
            left += 1
        array[left], array[right] = array[right], array[left]

    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)


def quick_sort_one(arr, left, right):
    value = arr[left]
    while left < right:
        while left < right and value <= arr[right]:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
        while left < right and value >= arr[left]:
            left += 1
        arr[left], arr[right] = arr[right], arr[left]
    return left


def quick_sort_without_recursion(arr):
    # 非递归实现: 栈
    stack_list = [(0, len(arr)-1)]
    while stack_list:
        left, right = stack_list.pop(-1)
        mid = quick_sort_one(arr, left, right)
        if mid > left:
            stack_list.append((left, mid-1))
        if mid < right:
            stack_list.append((mid+1, right))


if __name__ == '__main__':
    arr = [2, 3, 5, 4, 1, 7, 6]
    print(arr)
    quick_sort_without_recursion(arr)
    print(arr)
    # arr = [5, 4, 3, 7, 6]
    # quick_sort_one(arr, 0, len(arr)-1)
    # print(arr)

