#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
打开密码锁，每一次每个锁有向上、向下两种状态，所以每次一共8种
"""
import copy


def up_do(cur_string, i):
    # 某一位向上转
    string_ele = cur_string[i]
    if int(string_ele) == 9:
        new_value = 0
    else:
        new_value = int(string_ele) + 1
    new_string_list = []
    for j in range(len(cur_string)):
        if i == j:
            new_string_list.append(str(new_value))
        else:
            new_string_list.append(cur_string[j])
    return ''.join(new_string_list)


def down_do(cur_string, i):
    string_ele = cur_string[i]
    if int(string_ele) == 0:
        new_value = 9
    else:
        new_value = int(string_ele) - 1
    new_string_list = []
    for j in range(len(cur_string)):
        if i == j:
            new_string_list.append(str(new_value))
        else:
            new_string_list.append(cur_string[j])
    return ''.join(new_string_list)


def bfs(target, deadends):
    node_child_list = [['0000']]
    already_path = []  # 记录已经走过的路径
    depth = 0
    while len(node_child_list) != 0:
        level_node_list = node_child_list.pop(0)

        # 找到目标，终止
        if target in level_node_list:
            return depth

        child_level_node_list = []
        for node in level_node_list:
            already_path.append(node)
            for i in range(4):
                if up_do(node, i) not in deadends and up_do(node, i) not in already_path:
                    child_level_node_list.append(up_do(node, i))
                if down_do(node, i) not in deadends and down_do(node, i) not in already_path:
                    child_level_node_list.append(down_do(node, i))
        if child_level_node_list:
            node_child_list.append(child_level_node_list)
        depth += 1
    return -1


if __name__ == '__main__':
    # re = bfs('0202', ['0201', '0101', '0102', '1212', '2002'])
    # re = bfs('0009', ['8888'])
    re = bfs('8888', ['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'])
    print(re)