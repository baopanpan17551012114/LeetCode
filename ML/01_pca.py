# coding: utf-8
import numpy as np

data = [(2.5,2.4), (0.5,0.7), (2.2,2.9), (1.9,2.2), (3.1,3.0), (2.3, 2.7), (2, 1.6), (1, 1.1), (1.5, 1.6), (1.1, 0.9)]
x = [ele[0] for ele in data]
y = [ele[1] for ele in data]
# 中心化，每个维度向量减去其均值
x_mean, y_mean = round(np.mean(x), 2), round(np.mean(y), 2)
x_new = np.array(x - x_mean)
y_new = np.array(y - y_mean)
# 协方差矩阵
xxt = [[np.dot(x_new, x_new), np.dot(x_new, y_new)], [np.dot(y_new, x_new), np.dot(y_new, y_new)]]/np.array([9])
# print(np.cov(x_new, y_new))
# 特征值分解
value, vector = np.linalg.eig(xxt)
# print(value)
# print(vector)
# 取最大的特征值1.28402771对应特征向量w = [-0.6778734, -0.73517866]
data_new = np.dot(np.array([-0.6778734, -0.73517866]), np.array([x_new, y_new]))
print(np.shape(vector), np.shape(np.array([x_new, y_new])))
print(data_new)

# https://cloud.tencent.com/developer/article/1085126?from_column=20421&from=20421