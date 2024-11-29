import matplotlib.pyplot as plt

# 十月份支出数据
expenses = {
    "Food": 900,
    "Transport": 30,
    "books": 100,
    "Other": 300
}

# 提取标签和支出金额
labels = list(expenses.keys())
sizes = list(expenses.values())
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'purple']

# 饼状图 1：普通样式
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("October Expenses")
plt.show()

# 饼状图 2：突出某项支出（比如 Rent）
explode = [0.1, 0, 0, 0]  # 突出第一项支出
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode)
plt.title("October Expenses (Highlighted Food)")
plt.show()
