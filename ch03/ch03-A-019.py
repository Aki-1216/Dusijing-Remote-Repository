# 活动 14：continue 跳过正常城市并计数
cities_temps = [("北京", 28), ("上海", 32), ("广州", 36), ("哈尔滨", 22), ("武汉", 35)]

hot = 0
normal = 0
for name, temp in cities_temps:
    if temp < 35:
        print(f"{name} {temp}°C 正常，跳过")
        normal += 1
        continue
    print(f"{name} {temp}°C → 发高温预警")
    hot += 1

print(f"共检查 {hot + normal} 个城市：高温 {hot} 个，正常 {normal} 个")

# 挑战：不用 continue 的等价版本
for name, temp in cities_temps:
    if temp < 35:
        print(f"{name} {temp}°C 正常，跳过")
    else:
        print(f"{name} {temp}°C → 发高温预警")
