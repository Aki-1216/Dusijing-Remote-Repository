# 活动 16：循环嵌套与星号图案
# 1) 5×5 实心矩形
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

# 2) 直角三角形：第 i 行 i 个星号
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# 3) 数字三角形：第 i 行 1 到 i
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 挑战：倒直角三角形，5 行递减到 1
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
