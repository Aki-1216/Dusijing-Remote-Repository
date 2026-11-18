# 活动 13：循环输入城市名录（q/Q 退出、空输入跳过、list 查看）
cities = []
total = 0.0

while True:
    city = input("请输入城市名称（q/Q 退出，list 查看）：")
    if city in ("q", "Q"):
        break
    if city == "":
        print("城市名称不能为空，请重新输入")
        continue
    if city == "list":
        print("已录入：" + "、".join(cities) if cities else "尚未录入城市")
        continue
    temp = float(input(f"请输入{city}的气温："))
    cities.append(city)
    total += temp
    print(f"已记录第 {len(cities)} 个城市：{city} {temp}°C")

if cities:
    print(f"共 {len(cities)} 个城市，平均气温：{total / len(cities):.1f}°C")
else:
    print("本次没有有效数据")
print("录入结束")
