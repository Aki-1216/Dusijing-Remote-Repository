# 活动 12：break 找到就停 + 检查计数
cities_temps = [("北京", 28), ("上海", 32), ("广州", 36), ("哈尔滨", 22)]

checked = 0
for name, temp in cities_temps:
    checked += 1
    if temp >= 35:
        print(f"找到高温城市：{name} {temp}°C，立即发预警并停止扫描")
        break
    print(f"{name} {temp}°C 正常，继续")

print(f"共检查了 {checked} 个城市")
print("扫描结束")

# 挑战：不用 break，遍历全部找最高气温
max_name, max_temp = cities_temps[0]
for name, temp in cities_temps:
    if temp > max_temp:
        max_name, max_temp = name, temp
print(f"气温最高的城市：{max_name} {max_temp}°C")
