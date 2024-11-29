import pandas as pd
from sklearn.linear_model import LinearRegression

# 数据（1990-2005）
data = {
    'Year': [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005],
    'Population Growth Rate': [14.39, 12.98, 11.6, 11.45, 11.21, 10.55, 10.42, 10.06, 9.14, 8.18, 7.58, 6.95, 6.45, 6.01, 5.87, 5.89],
    'GDP': [18718, 21826, 26937, 35260, 48108, 59811, 70142, 78061, 83024, 88479, 98000, 108068, 119096, 135174, 159587, 184089],
    'CPI Growth Rate': [3.1, 3.4, 6.4, 14.7, 24.1, 17.1, 8.3, 2.8, -0.8, -1.4, 0.4, 0.7, -0.8, 1.2, 3.9, 1.8],
    'Per Capita GDP': [1644, 1519, 1644, 1893, 2311, 2998, 4044, 5046, 5846, 6420, 6796, 7159, 7858, 8622, 9398, 10542]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 提取自变量 X 和因变量 y
X = df[['GDP', 'CPI Growth Rate', 'Per Capita GDP']]
y = df['Population Growth Rate']

# 线性回归
model = LinearRegression()
model.fit(X, y)

# 显示回归系数和截距
print("回归系数:", model.coef_)
print("截距:", model.intercept_)
