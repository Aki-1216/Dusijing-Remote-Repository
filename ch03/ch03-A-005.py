# 活动 03：if-else 双分支 + 穿衣建议
temp = float(input("请输入气温："))

if temp >= 35:
    print(f"气温 {temp:.1f}°C，发高温预警")
    print("穿衣建议：轻薄透气")
else:
    print(f"气温 {temp:.1f}°C，天气正常")
    print("穿衣建议：常规着装")
