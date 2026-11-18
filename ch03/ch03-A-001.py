# 活动 01：气象站四级预警 + 高温城市计数
cities_temps = [("北京", 38), ("上海", 36), ("广州", 29), ("哈尔滨", 22),
                ("成都", 27), ("武汉", 41), ("西安", 33), ("乌鲁木齐", 32)]

hot_count = 0
for name, temp in cities_temps:
    if temp >= 40:
        level = "高温红色预警"
    elif temp >= 35:
        level = "高温橙色预警"
    elif temp >= 30:
        level = "天气炎热，注意防暑"
    else:
        level = "温度正常"
    print(f"{name} {temp}°C → {level}")
    if temp >= 35:              # 红、橙两档都算高温
        hot_count += 1

print(f"高温城市共 {hot_count} 个")
