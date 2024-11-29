import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

# 随机种子，确保结果可重复
np.random.seed(42)

student_number_last_two_digits = 32

# 生成10×15的高斯矩阵
mean = student_number_last_two_digits
std_dev = 1
matrix = np.random.normal(mean, std_dev, (10, 15))

# LU分解
P, L, U = la.lu(matrix)

# QR分解
Q, R = np.linalg.qr(matrix)

# 奇异值分解
U_svd, S, Vt = np.linalg.svd(matrix)

# 绘制分解结果
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

# LU分解的L和U矩阵
axes[0, 0].imshow(L, cmap='viridis')
axes[0, 0].set_title('LU-L')
axes[0, 1].imshow(U, cmap='viridis')
axes[0, 1].set_title('LU-U')

# QR分解的Q和R矩阵
axes[1, 0].imshow(Q, cmap='viridis')
axes[1, 0].set_title('QR-Q')
axes[1, 1].imshow(R, cmap='viridis')
axes[1, 1].set_title('QR-R')

plt.tight_layout()
plt.show()

# 显示奇异值
print("奇异值分解的奇异值:", S)
