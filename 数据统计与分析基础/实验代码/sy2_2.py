import numpy as np
import matplotlib.pyplot as plt

# 学号和区间 I
My_id = 225432
I = [My_id - 15, My_id + 15]
t = np.linspace(I[0], I[1], 500)

# 参数方程
x = np.sin(t) - t * np.cos(t)
y = np.cos(t) - t * np.sin(t)
z = t

# 绘制三维曲线
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='purple')
ax.set_title("3D Curve")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis (log scale)")
ax.grid(True)

# Z 轴对数刻度
ax.set_zscale('log')  # Z轴取对数
plt.show()
