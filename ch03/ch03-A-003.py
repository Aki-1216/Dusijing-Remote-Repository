# 活动 02：单分支 if、缩进与独立的湿度判断
temp = 33                       # 阈值 35 → 33
is_humid = 85

if temp >= 33:
    print(f"高温预警：气温超过 {temp}°C")
    print("请注意防暑降温")

print(f"当前气温：{temp}°C")

# 独立的 if：与上面的分支互不影响
if is_humid >= 80:
    print("湿度提醒：体感闷热，注意通风")

# 挑战：把第 2 行换成下一行即改为键盘输入
# temp = float(input("请输入气温："))
