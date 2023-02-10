#!/usr/bin/env python
# -*- coding:utf-8 -*-
import gc
import waste_memory

# 获取运行前gc引用对象数量
found_objects = gc.get_objects()
print('Before:', len(found_objects))

# 运行待测试代码的函数
hold_reference = waste_memory.run()
# 获取运行代码后gc引用对象数量
found_objects = gc.get_objects()
print('After: ', len(found_objects))
for obj in found_objects[:3]:
    print(repr(obj)[:100])