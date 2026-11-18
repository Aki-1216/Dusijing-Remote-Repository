# 活动 04：多分支预警分级（条件从严到宽）
temp = float(input("请输入气温："))

if temp >= 40:
    level = "高温红色预警"
elif temp >= 35:
    level = "高温橙色预警"
elif temp >= 33:
    level = "高温黄色预警"
elif temp >= 30:
    level = "天气炎热，注意防暑"
elif temp <= -8:
    level = "低温黄色预警"
elif temp <= -5:               # ≤-5 必须写在 ≤0 之前
    level = "低温蓝色预警"
elif temp <= 0:
    level = "低温蓝色预警"
else:
    level = "温度正常"

print(f"气温 {temp:.1f}°C → {level}")
