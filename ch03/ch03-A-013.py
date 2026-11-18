# 活动 09：累加器、奇偶和、平均值与计数
total = 0
even_sum = 0
odd_sum = 0
count3 = 0

for i in range(1, 101):
    total += i
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    if i % 3 == 0:
        count3 += 1

print(f"1~100 的和：{total}")
print(f"偶数和：{even_sum}，奇数和：{odd_sum}")
print(f"平均值：{total / 100:.1f}")
print(f"3 的倍数：{count3} 个")
