# coding: utf-8
import random
import math
from bisect import bisect_right

import numpy as np
from mealpy.evolutionary_based.GA import BaseGA

"""
N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
返回 6，选择前两件物品装进背包，总重量 3 ⼩于 W，可以获得最⼤价值6
"""


class Population:
    """
    遗传算法
    """
    def __init__(self, weights, values, total_weight):
        self.weights = weights
        self.values = values
        self.total_weight = total_weight
        self.chromosome_size = len(weights)  # 个体的染色体长度

        self.individuals = []  # 个体集合
        # 随机产生初始个体集，并将新一代个体、适应度、选择概率等集合以 0 值进行初始化
        v = 2 ** self.chromosome_size - 1
        for i in range(self.size):
            self.individuals.append([random.randint(0, v), random.randint(0, v)])

    def fitness_func(self, solution):
        """
        适应度函数
        :param solution:
        :return:
        """
        total_value = np.dot(solution, self.values)
        total_weight = np.dot(solution, self.weights)
        if total_weight > self.total_weight:
            return 0  # 超重，惩罚为0
        return total_value

    def select(self, solutions, n):
        """
        选择
        :return:
        """
        # 轮盘赌博机，按照概率选择
        tmp_value_list = []
        for solution in solutions:
            tmp_value = self.fitness_func(solution)
            tmp_value_list.append(tmp_value)

        # 前缀和
        front_value_list = [tmp_value_list[0]]
        for ele in tmp_value_list[1:]:
            front_value_list.append(front_value_list[-1] + ele)

        selected_solutions = []
        for i in range(n):
            random_value = random.randint(0, front_value_list[-1])
            index = bisect_right(front_value_list, random_value)
            selected_solutions.append(solutions[index])

    def cross(self, solution1, solution2):
        """
        交叉
        :return:
        """
        index = random.randint(1, self.chromosome_size-1)
        solution_new_1 = solution1[:index] + solution2[index:]
        solution_new_2 = solution2[:index] + solution1[index:]
        return solution_new_1, solution_new_2

    def mutate(self, solution):
        """
        变异
        :return:
        """
        index = random.randint(1, self.chromosome_size-1)
        solution[index] = 0 if solution[index] else 1
        return solution

    def evolve(self):
        """
        进化过程
        :return:
        """




if __name__ == '__main__':
    print([1, 2, 3]+[4])