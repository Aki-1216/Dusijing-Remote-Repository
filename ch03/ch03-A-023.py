# 活动 17：九九乘法表
# 1) 完整 9 行下三角表（含表头与分隔线）
print("九九乘法表")
print("=" * 60)
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}", end="\t")
    print()

# 2) 只打印乘积为偶数的式子（奇数跳过）
print("\n偶数版：")
for i in range(1, 10):
    for j in range(1, i + 1):
        if (i * j) % 2 == 0:
            print(f"{j}×{i}={i * j}", end="\t")
    print()

# 挑战：n×n 乘法表，n 由 input 输入
n = int(input("\n请输入 n："))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}", end="\t")
    print()
