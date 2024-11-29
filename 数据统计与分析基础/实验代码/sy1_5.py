# 遍历X, Y, Z的所有可能取值
for X in range(1, 10):  # X不能为0，因为它是一个数字的最高位
    for Y in range(0, 10):
        for Z in range(0, 10):
            # 计算XYZ和YZZ的值
            XYZ = 100 * X + 10 * Y + Z
            YZZ = 100 * Y + 10 * Z + Z

            # 检查是否满足XYZ + YZZ = 532
            if XYZ + YZZ == 532:
                print(f"X={X}, Y={Y}, Z={Z}")
