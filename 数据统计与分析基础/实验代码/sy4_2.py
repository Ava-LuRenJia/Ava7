import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# 加载数据，指定列名
columns = ['Class', 'Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash', 'Magnesium',
           'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins',
           'Color Intensity', 'Hue', 'OD280/OD315 of Diluted Wines', 'Proline']

# 读取 Wine 数据集
data = pd.read_csv(r'D:\python\SZFX\wine.data', header=None, names=columns)

# 提取特征数据（排除类别标签列）
X = data.iloc[:, 1:].values

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 进行 PCA 降维，保留所有主成分
pca = PCA(n_components=13)  # 保留所有成分
X_pca = pca.fit_transform(X_scaled)

# 查看各主成分的贡献率
explained_variance = pca.explained_variance_ratio_
print(f"各主成分的贡献率: {explained_variance}")

# 查看累计贡献率
cumulative_variance = np.cumsum(explained_variance)
print(f"累计贡献率: {cumulative_variance}")

# 找到贡献率之和大于 90%的成分
n_components = np.argmax(cumulative_variance >= 0.90) + 1
print(f"保留的主成分数: {n_components}")

# 提取贡献率和大于 90% 的主成分
pca = PCA(n_components=n_components)
X_pca_reduced = pca.fit_transform(X_scaled)

# 输出降维后的数据
print(f"降维后的数据:\n{X_pca_reduced}")
