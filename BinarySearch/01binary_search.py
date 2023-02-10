#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
寻找一个数
"""


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


def binary_search_left(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        print(left, right, mid)
        if nums[mid] == target:
            right = mid - 1  # 即使相等还是左移一位
        elif nums[mid] < target:  # left始终在right左侧，最终在左移一位相遇
            left = mid + 1        # 在左移一位相遇，肯定<target，left右移到正确位置
        elif nums[mid] > target:
            right = mid - 1
    if nums[left] != target or left > len(nums) - 1:
        return -1
    return left


def binary_search_right(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        print(left, right, mid)
        if nums[mid] == target:
            left = mid + 1  # 1、即使相等，left还是右移了一位
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:  # 2、right始终在left右边，最终在右移的一位上相遇
            right = mid - 1       # 3、在右移的一位相遇，肯定>target，right左移到正确位置
    if nums[right] != target or right < 0:
        return -1
    return right


if __name__ == '__main__':
    # re = binary_search([1, 2, 3, 4, 5], 1)
    # re = binary_search_left([1, 2, 4, 4, 4, 5], 1)
    re = binary_search_right([1, 2, 3, 4, 4, 5], 3)
    print(re)