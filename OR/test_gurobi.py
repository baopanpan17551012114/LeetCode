# coding:utf-8
import gurobipy as gp
from gurobipy import GRB

# 客户点数量
n = 5

# 车辆数量
m = 2

# 车辆容量限制
Q = 10

# 客户点的坐标
coordinates = [(0, 0), (2, 4), (5, 2), (7, 7), (10, 3)]

# 距离矩阵
distance_matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = ((coordinates[i][0] - coordinates[j][0]) ** 2 +
                                 (coordinates[i][1] - coordinates[j][1]) ** 2) ** 0.5

# 客户点的需求
demands = [0, 3, 5, 2, 4]

# 创建模型
model = gp.Model("CVRP")

# 创建变量
x = {}
for i in range(n):
    for j in range(n):
        for k in range(m):
            x[i, j, k] = model.addVar(vtype=GRB.BINARY, name=f"x_{i}_{j}_{k}")

# 设置目标函数
obj = gp.quicksum(distance_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))
model.setObjective(obj, GRB.MINIMIZE)

# 添加约束条件
# 每个客户点必须被访问且仅被访问一次
for i in range(1, n):
    model.addConstr(gp.quicksum(x[i, j, k] for j in range(n) for k in range(m)) == 1)

# 每辆车的路径必须从起始点开始，并在终点结束
for k in range(m):
    model.addConstr(gp.quicksum(x[0, j, k] for j in range(1, n)) == 1)
    model.addConstr(gp.quicksum(x[i, 0, k] for i in range(1, n)) == 1)

# 车辆容量限制
for k in range(m):
    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j, k] * demands[j] for j in range(n)) <= Q)

# 调用求解器
model.optimize()
