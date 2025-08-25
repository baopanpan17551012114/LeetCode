# coding: utf-8
import sys

import pandas as pd


def data_deel_scene(line):
    line = line.split('for')[1]
    scene_value = 0
    task_value = 0
    order_value = 0
    for ele in line.split(' '):
        if 'scene' in ele:
            scene_value = ele.split(':')[1]
        if 'task' in ele:
            task_value = ele.split(':')[1]
        if 'order' in ele:
            order_value = ele.split(':')[1]
    return scene_value

def data_deel_task(line):
    line = line.split('for')[1]
    scene_value = 0
    task_value = 0
    order_value = 0
    for ele in line.split(' '):
        if 'scene' in ele:
            scene_value = ele.split(':')[1]
        if 'task' in ele:
            task_value = ele.split(':')[1]
        if 'order' in ele:
            order_value = ele.split(':')[1]
    return task_value

def data_deel_order(line):
    line = line.split('for')[1]
    scene_value = 0
    task_value = 0
    order_value = 0
    for ele in line.split(' '):
        if 'scene' in ele:
            scene_value = ele.split(':')[1]
        if 'task' in ele:
            task_value = ele.split(':')[1]
        if 'order' in ele:
            order_value = ele.split(':')[1]
    order_value = order_value.replace('[', '').replace(']', '')
    return order_value


df = pd.read_csv('data/query_result_2025-04-02.csv', error_bad_lines=False)
df['order'] = df['message'].map(data_deel_order)
df['scene'] = df['message'].map(data_deel_scene)
df['task'] = df['message'].map(data_deel_task)
df = df[['time', 'scene', 'task', 'order']]
df.to_csv('data/query_result_2025-04-02_new.csv')