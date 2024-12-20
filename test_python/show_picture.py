# coding: utf-8
from matplotlib import pyplot as plt
import numpy as np

x = list(range(1, 6))
y = [e-3 for e in x]
y_1 = np.cbrt(y)
print(y_1)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 画两条线，并写明哪条线表示什么,设置线条样式
plt.plot(x, y_1, color="coral", linewidth=5)

# 设置x轴刻度
# _xtick_labels = ["pressure_{}".format(i) for i in x]
# plt.xticks(x, _xtick_labels)
# plt.yticks(range(0,9))

# 显示中文字体
# plt.rcParams['font.sans-serif'] = ['SimHei', ]

# 绘制网格,alpha设置网格透明度
# plt.grid(alpha=0.5, linestyle=':')

# 添加图例(在指定位置显示线条对应的含义)
# plt.legend(loc="upper left")
plt.show()

