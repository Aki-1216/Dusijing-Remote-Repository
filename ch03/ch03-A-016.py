# 活动 11：while True 录入系统（除零修复 + 最高值 + 范围校验）
print("=== 城市气温录入系统 ===")
total_temp = 0.0
city_count = 0
max_temp = -999.0
max_city = ""
city_names = ""

while True:
    city = input("请输入城市名称（输入q结束）：")
    if city == "q":
        break
    temp = float(input("请输入摄氏温度："))
    if temp < -50 or temp > 60:        # 合理范围校验
        print("温度超出 -50~60 范围，本条不录入")
        continue
    total_temp += temp
    city_count += 1
    if temp > max_temp:
        max_temp = temp
        max_city = city
    city_names += city + "、"
    print(f"已录入 {city_count} 个城市，当前平均气温：{total_temp / city_count:.1f}°C")

# 只有录入过城市才计算，避免除零
if city_count > 0:
    print(f"平均气温：{total_temp / city_count:.1f}°C")
    print(f"最高气温：{max_city} {max_temp:.1f}°C")
    print(f"本次录入：{city_names.rstrip('、')}")
else:
    print("本次没有录入任何城市")
print("录入完毕！")
