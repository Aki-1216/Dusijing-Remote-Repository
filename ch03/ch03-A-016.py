print("=== 城市气温录入系统 ===")
total_temp = 0
city_count = 0

while True:
    city = input("请输入城市名称（输入q结束）：")
    if city == "q":
        break  # 输入 q 就跳出循环
    temp = float(input("请输入摄氏温度："))
    total_temp = total_temp + temp
    city_count = city_count + 1
    print(f"已录入 {city_count} 个城市，当前平均气温：{total_temp/city_count:.1f}°C")

print(f"一共录入了 {city_count} 个城市，平均气温：{total_temp/city_count:.1f}°C")
print("录入完毕！")