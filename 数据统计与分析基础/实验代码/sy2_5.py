import numpy as np
import matplotlib.pyplot as plt

# 学号和区间 I
My_id = 225432
I = [My_id - 15, My_id + 15]
t = np.linspace(I[0], I[1], 500)

# 参数方程
x = np.sin(t) - t * np.cos(t)
y = np.cos(t) - t * np.sin(t)

# 绘制散点图
plt.figure(figsize=(10, 6))

# 散点图
plt.scatter(x, y, label="Scatter Points", color='red', s=10)

# 设置标题和标签
plt.title("Points")
plt.xlabel("x = sin(t) - t*cos(t)")
plt.ylabel("y = cos(t) - t*sin(t)")

# 显示图例
plt.legend()

# 显示网格
plt.grid()

# 展示图形
plt.show()
