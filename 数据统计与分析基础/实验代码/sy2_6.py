import numpy as np
import matplotlib.pyplot as plt

# 学号和区间 I
student_id = 225432
I = [student_id - 15, student_id + 15]
t = np.linspace(I[0], I[1], 500)

# 参数方程
x = np.sin(t) - t * np.cos(t)
y = np.cos(t) - t * np.sin(t)

# 绘制曲线图和阶梯图
plt.figure(figsize=(10, 6))

# 曲线图
plt.plot(x, y, label="Line Plot", linestyle='-', color='blue')

# 阶梯图
plt.step(x, y, label="Step Plot", linestyle='--', color='green')

# 设置标题和标签
plt.title("Line and Step Plots")
plt.xlabel("x = sin(t) - t*cos(t)")
plt.ylabel("y = cos(t) - t*sin(t)")

# 显示图例
plt.legend()

# 显示网格
plt.grid()

# 展示图形
plt.show()