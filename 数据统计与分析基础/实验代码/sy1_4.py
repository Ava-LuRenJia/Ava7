import numpy as np

# 生成两个服从标准正态分布的向量
vector1 = np.random.normal(loc=0, scale=1, size=100)
vector2 = np.random.normal(loc=0, scale=1, size=100)

# 复制向量用于对调后的结果
vector1_swapped = vector1.copy()
vector2_swapped = vector2.copy()

# 对偶数位进行对调 (Python索引从0开始，偶数位为索引1, 3, 5,...)
vector1_swapped[1::2], vector2_swapped[1::2] = vector2[1::2], vector1[1::2]

# 输出结果
print("原始向量1：")
print(vector1)
print("\n原始向量2：")
print(vector2)
print("\n对调后向量1：")
print(vector1_swapped)
print("\n对调后向量2：")
print(vector2_swapped)
