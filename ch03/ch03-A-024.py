# 活动 18：A-v3 菜单循环版温度转换（开尔文 + 计数 + 公式）
print("=" * 30)
print("    温度转换工具 v3")
print("=" * 30)

count = 0

while True:
    print("\n请选择功能：")
    print("1. 摄氏转华氏")
    print("2. 华氏转摄氏")
    print("3. 摄氏转开尔文")
    print("4. 查看换算公式")
    print("0. 退出程序")

    choice = input("请输入选项（0/1/2/3/4）：")

    if choice == "0":
        print(f"感谢使用，本次共转换 {count} 次，再见！")
        break
    elif choice == "1":
        c = float(input("请输入摄氏温度："))
        print(f"摄氏 {c:.2f}°C = 华氏 {c * 9 / 5 + 32:.2f}°F")
        count += 1
    elif choice == "2":
        f = float(input("请输入华氏温度："))
        print(f"华氏 {f:.2f}°F = 摄氏 {(f - 32) * 5 / 9:.2f}°C")
        count += 1
    elif choice == "3":
        c = float(input("请输入摄氏温度："))
        print(f"摄氏 {c:.2f}°C = 开尔文 {c + 273.15:.2f}K")
        count += 1
    elif choice == "4":
        print("换算公式：")
        print("  华氏 = 摄氏 × 9 / 5 + 32")
        print("  摄氏 = (华氏 - 32) × 5 / 9")
        print("  开尔文 = 摄氏 + 273.15")
    else:
        print("输入无效，请重新选择")
