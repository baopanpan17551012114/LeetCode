#!/usr/bin/env python
# -*- coding:utf-8 -*-


def quick_sort(arr: list, left: int, right: int):
    value = arr[left]
    while left < right:
        while left < right and arr[right] > value:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] < value:
            left += 1
        arr[right] = arr[left]

    arr[left] = value
    return left


def process(arr: list, left: int, right: int):
    index = quick_sort(arr, left, right)
    if index > left+1:
        process(arr, left, index-1)
    if index < right-1:
        process(arr, index+1, right)


if __name__ == '__main__':
    arr = [2, 3, 5, 4, 1, 7, 6]
    process(arr, 0, len(arr)-1)
    print(arr)