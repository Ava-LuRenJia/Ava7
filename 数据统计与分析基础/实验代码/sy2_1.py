import numpy as np
import matplotlib.pyplot as plt

# 学号和区间 I
My_id = 225432
I = [My_id - 15, My_id + 15]
t = np.linspace(I[0], I[1], 500)

# 1. 绘制 sin, cos, tan 函数曲线图
plt.figure(figsize=(10, 6))
plt.plot(t, np.sin(t), label='sin(t)', linestyle='-', color='blue')
plt.plot(t, np.cos(t), label='cos(t)', linestyle='--', color='green')
plt.plot(t, np.tan(t), label='tan(t)', linestyle='-.', color='red')
plt.ylim(-10, 10)  # 限制 tan 的纵轴范围，避免无穷值
plt.legend()
plt.title("Trigonometric Functions")
plt.xlabel("t")
plt.ylabel("Value")
plt.grid()
plt.show()