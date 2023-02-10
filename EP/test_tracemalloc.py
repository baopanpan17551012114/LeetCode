#!/usr/bin/env python
# -*- coding:utf-8 -*-
import gc
import os
import tracemalloc
import waste_memory

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()
x = waste_memory.run()

time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats[:5]:
    print(stat)

# tracemalloc.start(10)
# time1 = tracemalloc.take_snapshot()
# x = waste_memory.run()
# time2 = tracemalloc.take_snapshot()
# stats = time2.compare_to(time1, 'traceback')
# top = stats[0]
# print('Biggest offender is:')
# # 打印栈信息
# print('\n'.join(top.traceback.format()))