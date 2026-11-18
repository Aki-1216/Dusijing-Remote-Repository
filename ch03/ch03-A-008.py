# 活动 05：并列 if-elif + and 合并高温高湿
temp = float(input("请输入气温："))
humidity = float(input("请输入湿度（%）："))

is_hot = temp >= 35
is_humid = humidity >= 80

if temp >= 38:
    print("高温红色预警")
elif temp >= 35:
    print("高温橙色预警")
elif is_humid:
    print("湿度较大，体感闷热")
else:
    print("天气舒适")

if is_hot and is_humid:
    print("闷热预警：高温高湿，请注意防暑")
elif is_hot:
    print("干热预警：高温干燥，请注意补水")
