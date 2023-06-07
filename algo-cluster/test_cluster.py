#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 综合分类数据集
from numpy import where, unique
from sklearn.cluster import AffinityPropagation, AgglomerativeClustering, Birch, DBSCAN, KMeans, MiniBatchKMeans, \
    MeanShift, SpectralClustering
from sklearn.cluster._optics import OPTICS
from sklearn.datasets import make_classification
from matplotlib import pyplot
from sklearn.mixture import GaussianMixture


def data_and_show(model, train_flag):
    """

    :param model:
    :param train_flag:
    :return:
    """
    # 定义数据集, 2个特征,
    X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1,
                               random_state=4)

    if train_flag:
        model.fit(X)
        yhat = model.predict(X)
    else:
        yhat = model.fit_predict(X)
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个类的样本创建散点图
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
        # 绘制散点图
        pyplot.show()


if __name__ == '__main__':
    # # 1、亲和力聚类算法
    # model = AffinityPropagation(damping=0.9)
    # train_flag = 1

    # # 2、层次聚类算法
    # model = AgglomerativeClustering(n_clusters=2)
    # train_flag = 0

    # # 3、综合层次聚类算法
    # model = Birch(threshold=0.01, n_clusters=2)
    # train_flag = 1

    # # 4、DBSCAN聚类算法
    # model = DBSCAN(eps=0.30, min_samples=9)
    # train_flag = 0

    # # 5、K-均值聚类算法
    # model = KMeans(n_clusters=2)
    # train_flag = 1

    # # 6、Mini-Batch K-均值聚类算法
    # model = MiniBatchKMeans(n_clusters=2)
    # train_flag = 1

    # # 7、均值漂移聚类算法
    # model = MeanShift()
    # train_flag = 0

    # # 8、OPTICS 聚类算法
    # model = OPTICS(eps=0.8, min_samples=10)
    # train_flag = 0

    # # 9、光谱聚类算法
    # model = SpectralClustering(n_clusters=2)
    # train_flag = 0

    # 10、高斯混合模型聚类算法
    model = GaussianMixture(n_components=2)
    train_flag = 1
    data_and_show(model, train_flag)
