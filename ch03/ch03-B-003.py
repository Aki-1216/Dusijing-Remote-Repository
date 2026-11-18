# ch03-B-003
# B-v3 奶茶店循环点单（挑战层）
# 功能：加料选择、undo 撤销上一杯、统计当天营业总额和订单数
# 姓名：__________  学号：__________  班级：__________  日期：__________

import random

# 当天营业统计
day_total = 0
day_orders = 0

print("=" * 30)
print("   欢迎来到校园奶茶店")
print("=" * 30)

# 循环接订单
while True:
    # 新订单
    order_id = random.randint(100000, 999999)
    print(f"\n--- 订单 {order_id} ---")

    is_member = input("是否会员？（是/否，直接回车默认否）：")

    receipt = ""
    total = 0
    count = 0

    # 保存上一杯信息，用于 undo
    last_name = ""
    last_subtotal = 0
    last_line = ""

    # 循环点单
    while True:
        name = input("请输入奶茶名称（q结束/undo撤销上一杯）：")
        if name == 'q':
            break
        if name == 'undo':
            if last_name:
                total -= last_subtotal
                count -= 1
                receipt = receipt.replace(last_line + "\n", "", 1)
                print(f"已撤销：{last_name}")
                last_name = ""
            else:
                print("没有可撤销的订单")
            continue

        # 杯型
        cup = input("杯型（1-中杯/2-大杯+3/3-超大杯+5）：")
        if cup == '2':
            cup_extra = 3
            cup_name = "大杯"
        elif cup == '3':
            cup_extra = 5
            cup_name = "超大杯"
        else:
            cup_extra = 0
            cup_name = "中杯"

        price = float(input("请输入单价："))
        qty = int(input("请输入数量："))

        # 加料
        topping = 0
        t_str = ""
        if input("加珍珠？(y/n)：") == 'y':
            topping += 2
            t_str += "珍珠 "
        if input("加椰果？(y/n)：") == 'y':
            topping += 1.5
            t_str += "椰果 "
        if input("加红豆？(y/n)：") == 'y':
            topping += 2
            t_str += "红豆"

        unit_price = price + cup_extra + topping
        subtotal = unit_price * qty
        total += subtotal
        count += qty

        line = f"{name}({cup_name})".ljust(10) + f"{unit_price:>8.2f}{qty:>6}{subtotal:>8.2f}"
        receipt += line + "\n"

        # 保存上一杯
        last_name = name
        last_subtotal = subtotal
        last_line = line

    # 满减
    if total >= 80:
        discount = 15
    elif total >= 50:
        discount = 8
    elif total >= 30:
        discount = 3
    else:
        discount = 0

    after = total - discount
    final = after * 0.9 if is_member == "是" else after

    # 输出小票
    print("\n" + "=" * 30)
    print(f"  订单编号：{order_id}")
    print("        校园奶茶店")
    print("=" * 30)
    print(f"{'商品':<10}{'单价':>8}{'数量':>6}{'小计':>8}")
    print("-" * 30)
    print(receipt, end="")
    print("-" * 30)
    print(f"{'原价合计：':>22}{total:>8.2f}")
    print(f"{'满减优惠：':>22}{discount:>8.2f}")
    print(f"{'实付金额：':>22}{final:>8.2f}")
    print("=" * 30)

    # 累计当天营业
    day_total += final
    day_orders += 1
    print(f"当天已完成 {day_orders} 单，营业总额：{day_total:.2f} 元")

    # 继续接单？
    if input("\n是否接下一单？（y/n）：") != 'y':
        break

print("\n        谢谢光临，欢迎下次再来！")
