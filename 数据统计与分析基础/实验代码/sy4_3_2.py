from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子，保证结果可复现
np.random.seed(42)

# 生成每个类的数据（30个样本），每个类的均值和方差不同，且有所交叉
class1 = np.random.normal(loc=[3, 3], scale=[1, 1], size=(30, 2))
class2 = np.random.normal(loc=[5, 5], scale=[2, 2], size=(30, 2))
class3 = np.random.normal(loc=[7, 7], scale=[1.5, 1.5], size=(30, 2))

# 合并所有类别的数据
X = np.vstack([class1, class2, class3])


# 定义绘图函数
def plot_kmeans(X, k, ax):
    kmeans = KMeans(n_clusters=k, random_state=42)
    y_kmeans = kmeans.fit_predict(X)

    # 绘制每个聚类的数据点
    ax.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', alpha=0.6)

    # 绘制聚类中心
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X',
               label='Centroids')

    ax.set_title(f'KMeans Clustering with {k} clusters')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend()


# 创建子图
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 对数据进行3类、4类和5类的KMeans聚类并绘制结果
plot_kmeans(X, 3, axs[0])
plot_kmeans(X, 4, axs[1])
plot_kmeans(X, 5, axs[2])

# 显示图像
plt.tight_layout()
plt.show()
