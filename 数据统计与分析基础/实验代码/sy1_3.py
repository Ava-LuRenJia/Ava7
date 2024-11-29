def grade_to_gpa(score):
    """
    将成绩转化为绩点的函数。
    :param score: 分数 (0-100)
    :return: 对应的绩点
    """
    if score >= 90:
        return 4.0
    elif score >= 85:
        return 3.7
    elif score >= 80:
        return 3.3
    elif score >= 75:
        return 3.0
    elif score >= 70:
        return 2.7
    elif score >= 65:
        return 2.3
    elif score >= 60:
        return 2.0
    else:
        return 0.0


# 调用函数并生成绩点
scores = [98, 93, 89, 73, 66]
gpas = [grade_to_gpa(score) for score in scores]

# 输出结果
for score, gpa in zip(scores, gpas):
    print(f"分数: {score}, 绩点: {gpa:.1f}")
