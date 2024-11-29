from scipy.optimize import linprog

# 目标函数的系数
c = [-1, -0.8, -1.2]  # 因为我们要最小化 -X1 - 0.8X2 - 1.2X3

# 不等式约束的系数矩阵
A = [
    [1, -1, 1],
    [3, 2, 4],
    [3, 2, 0]
]

# 不等式约束的右侧常数
b = [30, 42, 30]

# 变量的上下界
x_bounds = (0, None)
bounds = [x_bounds, x_bounds, x_bounds]

# 求解优化问题
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# 输出结果
print("最优解:", res.x)
print("最优目标函数值:", res.fun)

# 找到有效约束
for i, slack in enumerate(res.slack):
    if slack == 0:  # 如果松弛变量为0，说明该约束是有效的
        print(f"约束 {i + 1} 是有效约束")
