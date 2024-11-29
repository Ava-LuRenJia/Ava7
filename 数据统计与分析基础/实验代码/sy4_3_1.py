import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子，保证结果可复现
np.random.seed(42)

# 生成每个类的数据（30个样本），每个类的均值和方差不同，且有所交叉
# 类别1: 均值 (3, 3)，方差较小
class1 = np.random.normal(loc=[3, 3], scale=[1, 1], size=(30, 2))

# 类别2: 均值 (5, 5)，方差较大，与类别1略有交叉
class2 = np.random.normal(loc=[5, 5], scale=[2, 2], size=(30, 2))

# 类别3: 均值 (7, 7)，方差较大，与类别2略有交叉
class3 = np.random.normal(loc=[7, 7], scale=[1.5, 1.5], size=(30, 2))

# 合并所有类别的数据
X = np.vstack([class1, class2, class3])
y = np.array([0] * 30 + [1] * 30 + [2] * 30)  # 类别标签

# 绘制数据点
plt.figure(figsize=(8, 6))

# 绘制每个类别的数据点
plt.scatter(class1[:, 0], class1[:, 1], color='red', label='Class 1', alpha=0.6)
plt.scatter(class2[:, 0], class2[:, 1], color='blue', label='Class 2', alpha=0.6)
plt.scatter(class3[:, 0], class3[:, 1], color='green', label='Class 3', alpha=0.6)

# 设置标题和标签
plt.title('Generated Data with 3 Classes')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

# 显示图像
plt.show()
