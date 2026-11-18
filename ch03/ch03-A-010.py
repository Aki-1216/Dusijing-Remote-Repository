# 活动 07：顺序结构改写为循环
# 原版：5 行 print
print(1)
print(2)
print(3)
print(4)
print(5)

# for 版（3 行）
for i in range(1, 6):
    print(i)

# while 版（初始化 + 自增）
i = 1
while i <= 5:
    print(i)
    i += 1

# 挑战：1~100 的偶数，一行一个
for i in range(2, 101, 2):
    print(i)
