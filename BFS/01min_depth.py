#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""判断⼀棵⼆叉树的最⼩⾼度"""


class Node:
    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def get_min_depth(root):
    if root is None:
        return 0

    depth = 1
    level_node_list = [[root]]
    while len(level_node_list) != 0:
        # 模拟队列，先进先出
        node_list = level_node_list.pop(__index=0)
        # 层次遍历
        chile_level_node_list = []
        for node in node_list:
            if node.left_child is None and node.right_child is None:
                # 判断是否到达终点，层次遍历遇到对第一个叶子节点，就是深度
                return depth
            # 将相邻节点加⼊队列
            if node.left_child is not None:
                chile_level_node_list.append(node.left_child)
            if node.right_child is not None:
                chile_level_node_list.append(node.right_child)
        # 将下一层的节点列表存入总列表
        level_node_list.append(chile_level_node_list)  # 可以不采用列表，因为每次到外层循环时，都是进入下一层；只要在开始获取size
        depth += 1
    return depth


if __name__ == '__main__':
    root = None
    get_min_depth(root)