import numpy as np
import matplotlib.pyplot as plt

# 过去12个月的花费数据（这里是示例数据，可以替换成你的实际数据）
months = np.arange(1, 13)  # 12个月
expenditure_WeiXin = [3742.13, 2257.99, 4980.12, 1805.65, 2526.10, 2002.59, 3579.46, 1142.75, 2285.99, 1071.80, 719.48, 1462.10]

# 拟合一次、二次、三次曲线
coeffs_1 = np.polyfit(months, expenditure_WeiXin, 1)
coeffs_2 = np.polyfit(months, expenditure_WeiXin, 2)
coeffs_3 = np.polyfit(months, expenditure_WeiXin, 3)

# 创建拟合曲线
fit_1 = np.polyval(coeffs_1, months)
fit_2 = np.polyval(coeffs_2, months)
fit_3 = np.polyval(coeffs_3, months)

# 绘制数据和拟合曲线
plt.plot(months, expenditure_WeiXin, 'bo', label='actual expend')  # 原始数据
plt.plot(months, fit_1, 'r-', label='Fit the curve once')
plt.plot(months, fit_2, 'g--', label='Quadratic fitting curves')
plt.plot(months, fit_3, 'b-.', label='Cubic fitting curves')

plt.xlabel('month')
plt.ylabel('expend')
plt.legend()
plt.show()
