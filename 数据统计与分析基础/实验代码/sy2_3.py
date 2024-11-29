import numpy as np
import matplotlib.pyplot as plt

# 随机生成班级成绩，50个学生的成绩范围在 40 到 100 之间
np.random.seed(42)  # 保持结果一致
scores = np.random.randint(40, 101, 50)  # 生成 50 个成绩，范围为 40 到 100

# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(scores, bins=10, edgecolor='black', color='skyblue', range=(40, 100))
plt.title("Class Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()
