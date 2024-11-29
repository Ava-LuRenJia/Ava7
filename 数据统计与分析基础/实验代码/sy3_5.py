import numpy as np

months = np.arange(1, 13)  # 12个月
# 过去12个月的花费数据
data = np.array([3742.13, 2257.99, 4980.12, 1805.65, 2526.10, 2002.59, 3579.46, 1142.75, 2285.99, 1071.80, 719.48, 1462.10])

# 最大似然估计：均值和方差
mu_mle = np.mean(data)
sigma_mle = np.std(data, ddof=0)

print(f"均值的最大似然估计: {mu_mle}")
print(f"方差的最大似然估计: {sigma_mle ** 2}")
