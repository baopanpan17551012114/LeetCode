import numpy as np
from mealpy.evolutionary_based import GA


# 背包问题的定义
def knapsack_fitness(solution, weight, value, max_weight):
    solution = [1 if ele > 0.5 else 0 for ele in solution]
    total_value = np.dot(solution, value)
    total_weight = np.dot(solution, weight)
    if total_weight > max_weight:
        return -1  # 超重，惩罚为-1
    return total_value


# 背包问题参数
weights = np.array([2, 3, 4, 5])  # 物品的重量
values = np.array([3, 4, 5, 6])  # 物品的价值
max_weight = 5  # 背包的最大承重

# 创建背包问题
problem = {
    "fit_func": lambda solution: knapsack_fitness(solution, weights, values, max_weight),
    "lb": [0, 0, 0, 0],  # 解的下界
    "ub": [1, 1, 1, 1],  # 解的上界
    "minmax": "max",  # 最大化问题
}

# 创建遗传算法实例
model = GA.BaseGA(epoch=100, pop_size=50, pc=0.7, pm=0.1)

# 求解背包问题
best_solution, best_fitness = model.solve(problem)
print(f"Best Solution: {best_solution}")
print(f"Best Fitness: {best_fitness}")
