import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 设置随机种子，保证结果可复现
np.random.seed(42)

# 生成两个类别的数据，每个类包含30个样本，且完全不交叉
class1 = np.random.normal(loc=[2, 2], scale=[0.5, 0.5], size=(30, 2))  # 类别1，均值(2, 2)
class2 = np.random.normal(loc=[6, 6], scale=[0.5, 0.5], size=(30, 2))  # 类别2，均值(6, 6)

# 合并所有类别的数据
X = np.vstack([class1, class2])
y = np.array([0] * 30 + [1] * 30)  # 类别标签

# 创建并训练SVM模型
clf = svm.SVC(kernel='linear')
clf.fit(X, y)

# 获取所有支撑向量
support_vectors = clf.support_vectors_

# 绘制数据点
plt.figure(figsize=(8, 6))

# 绘制类别1和类别2的数据点
plt.scatter(class1[:, 0], class1[:, 1], color='red', label='Class 1', alpha=0.6)
plt.scatter(class2[:, 0], class2[:, 1], color='blue', label='Class 2', alpha=0.6)

# 绘制支撑向量
plt.scatter(support_vectors[:, 0], support_vectors[:, 1], color='green', marker='X', s=150, label='Support Vectors')

# 绘制决策边界
xx, yy = np.meshgrid(np.linspace(-1, 8, 100), np.linspace(-1, 8, 100))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 绘制决策边界和边界间隔
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='black')
plt.contour(xx, yy, Z, levels=[-1, 1], linewidths=1, colors='black', linestyles='dashed')

# 设置标题和标签
plt.title('SVM Classification with Support Vectors')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

# 显示图像
plt.show()
