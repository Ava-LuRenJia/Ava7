from scipy.stats import binom

# 设定参数
n = 50  # 射击次数
p = 0.1  # 每次射击的命中概率

# 计算击中10次以上且40次以下的概率
prob = binom.cdf(40, n, p) - binom.cdf(10, n, p)
print(f"击中10次以上且40次以下的概率是: {prob}")
