# -*- coding: utf-8 -*-
import random


class Life(object):
    # 初始化
    def __init__(self, gene = None):
        self.gene = gene
        self.score = -1.0

    # 设置评估分数
    def setScore(self, v):
        self.score = v


# TSP问题
class MyTSP(object):

    # 初始化
    def __init__(self, gene_length=6, overlapping_rate=0.7, mutation_rate=0.03, life_count=30, max_iteration=4000):

        self.overlapping_rate = overlapping_rate            # 交叉率
        self.mutation_rate = mutation_rate                  # 突变率
        self.mutation_count = 0                             # 突变次数
        self.generation = 0                                 # 进化代数
        self.lives = []                                     # 生命集合
        self.bounds = 0.0                                   # 得分总数
        self.best = None                                    # 种群每代中的最优个体
        self.best_gene = []                                 # 所有代种群中的最优基因
        self.best_gene_distance = 1e20                      # 所有代种群中的最优基因所对应的路径长度
        self.life_count = life_count                        # 生命个数
        self.gene_length = gene_length                      # 基因长度，此处即为城市个数
        self.max_iteration = max_iteration
        self.min_distance = []

        # 创造生命集
        for _ in range(self.life_count):
            self.lives.append(Life(self.make_life()))

        # 读取各城市间的距离
        self.dist_matrix = [[0, 1579, 1579, 1579, 18307, 1579, 13294], [1579, 0, 0, 0, 19789, 0, 14863],
                           [1579, 0, 0, 0, 19789, 0, 14863], [1579, 0, 0, 0, 19789, 0, 14863],
                           [18307, 19789, 19789, 19789, 0, 19789, 6332],
                           [1579, 0, 0, 0, 19789, 0, 14863],
                           [13294, 14863, 14863, 14863, 6332, 14863, 0]]

        print(self.lives[6].gene)
        print(self.distance(self.lives[6].gene))

    # 进化计算
    def evolve(self):
        while self.generation < self.max_iteration:
            # 下一步进化
            self.next()
            self.min_distance.append(self.distance(self.best.gene))
            if self.distance(self.best.gene) < self.best_gene_distance:
                self.best_gene_distance = self.distance(self.best.gene)
                self.best_gene = self.best.gene
            if self.generation % 200 == 0:
                print("迭代次数：%d, 变异次数%d, 最佳路径总距离：%d" % (self.generation, self.mutation_count, self.distance(self.best.gene)))
        print(self.best_gene)
        print(self.best_gene_distance)
        return

    # 创造新生命
    def make_life(self):
        lst = [i for i in range(self.gene_length)]
        # 随机顺序
        random.shuffle(lst)
        return lst

    # 演化至下一代
    def next(self):
        # 评估群体
        self.judge()
        # 新生命集
        newLives = []
        # 将最好的父代加入竞争
        newLives.append(Life(self.best.gene))
        # 产生新的生命集个体
        while(len(newLives) < self.life_count):
            newLives.append(self.bear())
        # 更新新的生命集
        self.lives = newLives
        self.generation += 1

    # 评价函数
    def judge(self):
        self.bounds = 0.0
        self.best = Life()
        self.best.setScore(-1.0)
        for lf in self.lives:
            lf.score = 1.0/self.distance(lf.gene)
            if lf.score > self.best.score:
                self.best = lf
            self.bounds += lf.score

    # 得到当前顺序下连线总长度
    def distance(self, order):
        distance = 0
        for i in range(-1, self.gene_length - 1):
            i1, i2 = order[i], order[i + 1]
            distance += self.get_city_distance(self.dist_matrix, self.gene_length, i1, i2)
        return distance

    def get_city_distance(self, dist_matrix, n, i, j):
        if i == j:
            return 0
        elif i > j:
            i, j = j, i
        print(int(i * (2 * n - i - 1)/2 + j - i - 1), (i * (2 * n - i - 1)/2 + j - i - 1))
        return dist_matrix[int(i * (2 * n - i - 1)/2 + j - i - 1)]

    # 产生后代
    def bear(self):
        lf1 = self.get_onelife()
        lf2 = self.get_onelife()
        # 交叉
        r = random.random()
        if r < self.overlapping_rate:
            gene = self.overlapping_func(lf1, lf2)
        else:
            gene = lf1.gene
        # 突变
        r = random.random()
        if r < self.mutation_rate:
            gene = self.mutation_func(gene)
            self.mutation_count += 1
        # 返回生命体
        return Life(gene)

    # 根据得分情况，随机取得一个个体，机率正比于个体的score属性
    def get_onelife(self):
        # 轮盘
        r = random.uniform(0, self.bounds)
        for lf in self.lives:
            r -= lf.score;
            if r <= 0:
                return lf

    # 交叉函数：选择lf2序列前子序列交叉到lf1前段，删除重复元素
    def overlapping_func(self, lf1, lf2):
        p2 = random.randint(1, self.gene_length - 1)
        # 截取if2
        g1 = lf2.gene[0:p2] + lf1.gene
        g11 = []
        for i in g1:
            if i not in g11:
                g11.append(i)
        return g11

    # 变异函数:选择两个不同位置基因交换，第一个选择的基因重新加入到序列尾端
    def mutation_func(self, gene):
        p1 = random.randint(0, self.gene_length - 1)
        p2 = random.randint(0, self.gene_length - 1)
        while p2 == p1:
            p2 = random.randint(0, self.gene_length - 1)
        gene[p1], gene[p2] = gene[p2], gene[p1]
        gene.append(gene[p2])
        del gene[p2]
        return gene


import matplotlib.pyplot as plt

overlapping_rate = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 0.9, 1.0]
mutation_rate = [0.005, 0.01, 0.03, 0.05, 0.07, 0.1, 0.2, 0.4, 0.7, 1.0]
life_count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yy = []

for i in range(len(overlapping_rate)):
    tsp = MyTSP(gene_length = 28, overlapping_rate = overlapping_rate[i], mutation_rate = 0.03, life_count = 30, max_iteration = 40)
    tsp.evolve()
    yy.append(tsp.best_gene_distance)
plt.figure('overlapping rate and minimum distance')
plt.plot(overlapping_rate, yy)
plt.xlabel('overlapping rate')
plt.ylabel("minimum distance of all generations")

yy = []
for i in range(len(mutation_rate)):
    tsp = MyTSP(gene_length = 28, overlapping_rate = 0.7, mutation_rate = mutation_rate[i], life_count = 30, max_iteration = 40)
    tsp.evolve()
    yy.append(tsp.best_gene_distance)
plt.figure("mutation rate and minimum distance")
plt.plot(mutation_rate, yy)
plt.xlabel('mutation rate')
plt.ylabel("minimum distance of all generations")

yy = []
for i in range(len(life_count)):
    tsp = MyTSP(gene_length = 28, overlapping_rate = 0.7, mutation_rate = 0.03, life_count = life_count[i], max_iteration = 40)
    tsp.evolve()
    yy.append(tsp.best_gene_distance)
plt.figure('life count of population and minimum distance')
plt.plot(life_count, yy)
plt.xlabel('life count of population')
plt.ylabel("minimum distance of all generations")

yy = []
tsp = MyTSP(28, 0.5, 0.03, 30, 40)
tsp.evolve()
plt.figure('number of generation and minimum distance')
plt.plot(range(1, tsp.max_iteration + 1), tsp.min_distance)
plt.xlabel('number of generation')
plt.ylabel("minimum distance of every generation")

plt.show()