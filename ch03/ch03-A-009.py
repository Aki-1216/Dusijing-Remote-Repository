temp = 36

# 第一段：缩进正确，两条 print 同层
if temp >= 35:
    print("高温预警")
    print("请注意防暑")
print(f"气温：{temp}°C")
# 挑战：把上面这行缩进 4 格进 if，temp = 30 时连气温都不打印

# 第二段：原第 10 行缩进 6 格，已改为 4 格
if temp >= 35:
    print("高温预警")
    print("请注意防暑")
