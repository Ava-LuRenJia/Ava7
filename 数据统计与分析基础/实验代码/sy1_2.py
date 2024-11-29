def find_numbers():
    results = []
    for num in range(1, 1000):
        # 检查是否是13的倍数
        if num % 13 == 0:
            results.append(num)
        # 检查是否前两位数字是13
        elif str(num).zfill(3)[:2] == "13":
            results.append(num)

    # 输出结果
    print("符合条件的数字如下：")
    print(results)
    print(f"总共有 {len(results)} 个符合条件的数字。")


if __name__ == "__main__":
    find_numbers()
