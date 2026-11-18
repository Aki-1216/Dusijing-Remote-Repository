# 活动 15：break / continue 六段对比
# 代码1
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=" ")
print()

# 代码2
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print()

# 代码3
i = 1
while i <= 5:
    if i == 3:
        break
    print(i, end=" ")
    i += 1
print()

# 代码4（已修复）：continue 之前先自增
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print()

# 代码5
for i in range(1, 6):
    print(i, end=" ")
    if i == 3:
        break
print()

# 代码6
for i in range(1, 6):
    print(i, end=" ")
    if i == 3:
        continue
print()

# 挑战：给死循环加保护计数器
i = 1
guard = 0
while i <= 5:
    guard += 1
    if guard > 10:
        print("检测到死循环，已自动退出")
        break
    if i == 3:
        continue
    print(i, end=" ")
    i += 1
print()
