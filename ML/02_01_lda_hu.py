# coding: utf-8
import sys

import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()  # 直接从datasets 导出数据
X, y = iris.data, iris.target  # 切分数据集

# 类内散度矩阵
s_w = np.zeros((4, 4))
for cl in range(3):
    matrix_tmp = np.zeros((4, 4))
    vec = np.mean(X[y == cl], axis=0)
    # 每个类别对应feature减去均值
    vec_del_mean = X[y == cl]-vec
    for i in range(4):
        for j in range(4):
            # np.dot可以自动转置
            matrix_tmp[i, j] = np.dot(vec_del_mean[:, i], vec_del_mean[:, j])
    s_w += matrix_tmp

# 类间散度矩阵
mean_vec = np.mean(X, axis=0)
s_b = np.zeros((4, 4))
for cl in range(3):
    N = np.count_nonzero(y == cl)
    mean_vec_cl = np.mean(X[y == cl], axis=0)
    res_vec = (mean_vec_cl - mean_vec).reshape(4, 1)
    value = N * np.dot(res_vec, res_vec.T)
    s_b += value

# s_w矩阵的逆矩阵 点乘 s_b
t_s = np.dot(np.linalg.inv(s_w), s_b)
values, vectors = np.linalg.eig(t_s)
print(values)

eig_pairs = [(np.abs(values[i]), vectors[:, i]) for i in range(len(values))]
eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
W = np.hstack((eig_pairs[0][1].reshape(4, 1), eig_pairs[1][1].reshape(4, 1)))
X = np.dot(X, W)  # 新的X, y不变
print(X.shape)





