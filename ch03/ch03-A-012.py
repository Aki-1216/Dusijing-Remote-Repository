# 活动 08：range 三种写法
for i in range(1, 6):          # 1~5
    print(i)

for i in range(5):             # 0~4
    print(i)

for i in range(2, 101, 2):     # 1~100 的偶数
    print(i, end=" ")
print()

for i in range(5, 0, -1):      # 倒序 5~1
    print(i, end=" ")
print()

# 挑战：先打 5 个星号，再打 100 到 10
for i in range(5):
    print("*", end="")
print()
for i in range(100, 0, -10):
    print(i, end=" ")
print()
