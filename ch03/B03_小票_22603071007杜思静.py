"""
实训3：项目名称-奶茶店循环点单 (B-v3)
姓名：杜思静
学号：22603071007
班级：26数管
完成日期：2026-11-22
"""

import random

print("======= 欢迎使用喵喵奶茶店点单系统 (B-v3) =======")
print("点单时输入 q 结束本单，输入 undo 撤销上一杯")

# 当天营业统计（程序运行期间累计）
day_total = 0.0
day_orders = 0

while True:
    order_id = random.randint(100000, 999999)      # 6 位随机订单编号
    print(f"\n===== 新订单 {order_id} =====")
    is_member = input("是否为本店会员？(y/n)：").strip().lower() == "y"

    total = 0.0        # 本单原价合计
    cups = 0           # 本单杯数
    lines = []         # 每杯明细
    last_total = 0.0   # 上一杯，用于 undo
    last_qty = 0
    last_name = ""
    has_last = False

    # 循环点单
    while True:
        name = input("\n请输入奶茶名称（q 结束 / undo 撤销上一杯）：").strip()
        if name == "q":
            break
        if name == "undo":
            if has_last:
                total -= last_total
                cups -= last_qty
                lines.pop()
                print(f"已撤销：{last_name}（-{last_total:.2f} 元）")
                has_last = False
            else:
                print("当前没有可撤销的订单")
            continue
        if name == "":
            print("奶茶名称不能为空")
            continue

        # 杯型：大杯 +3，超大杯 +5
        cup = input("杯型（1-中杯 / 2-大杯+3 元 / 3-超大杯+5 元）：").strip()
        if cup == "2":
            cup_extra, cup_name = 3.0, "大杯"
        elif cup == "3":
            cup_extra, cup_name = 5.0, "超大杯"
        else:
            cup_extra, cup_name = 0.0, "中杯"

        price = float(input("请输入单价："))
        qty = int(input("请输入数量："))

        # 加料（可多选）
        topping = 0.0
        toppings = []
        if input("加珍珠？(+2 元, y/n)：").strip().lower() == "y":
            topping += 2.0
            toppings.append("珍珠")
        if input("加椰果？(+1.5 元, y/n)：").strip().lower() == "y":
            topping += 1.5
            toppings.append("椰果")
        if input("加红豆？(+2 元, y/n)：").strip().lower() == "y":
            topping += 2.0
            toppings.append("红豆")

        unit_price = price + cup_extra + topping
        subtotal = unit_price * qty
        total += subtotal
        cups += qty

        item = f"{name}({cup_name}"
        if toppings:
            item += "，" + "+".join(toppings)
        item += ")"
        line = f"{item:<20}{unit_price:>8.2f}{qty:>5}{subtotal:>9.2f}"
        lines.append(line)
        print(f"已加入：{item} ×{qty}，小计 {subtotal:.2f} 元")

        last_total, last_qty, last_name = subtotal, qty, name
        has_last = True

    if cups == 0:
        print("本单未点任何奶茶，已取消")
    else:
        # 满减：满 30 减 3，满 50 减 8，满 80 减 15
        if total >= 80:
            discount = 15.0
        elif total >= 50:
            discount = 8.0
        elif total >= 30:
            discount = 3.0
        else:
            discount = 0.0

        after_discount = total - discount
        final = after_discount * 0.9 if is_member else after_discount   # 会员满减后再 9 折

        # 格式化小票
        print("\n" + "=" * 44)
        print(f"{'喵喵奶茶店订单小票':^38}")
        print(f"订单编号：{order_id}")
        print(f"顾客类型：{'会员（满减后再 9 折）' if is_member else '普通顾客'}")
        print("=" * 44)
        print(f"{'商品':<20}{'单价':>8}{'数量':>5}{'小计':>9}")
        print("-" * 44)
        print("\n".join(lines))
        print("-" * 44)
        print(f"{'杯数：':<20}{cups:>22}")
        print(f"{'原价合计：':<20}{total:>22.2f}")
        print(f"{'满减优惠：':<20}{discount:>22.2f}")
        if is_member:
            print(f"{'会员 9 折：':<20}{after_discount * 0.1:>22.2f}")
        print(f"{'实付金额：':<20}{final:>22.2f}")
        print("=" * 44)

        day_total += final
        day_orders += 1
        print(f"当天已完成 {day_orders} 单，营业总额 {day_total:.2f} 元")

    if input("\n是否继续下一单？(y/n)：").strip().lower() != "y":
        break

print("\n" + "=" * 44)
print(f"今日共完成 {day_orders} 单，营业总额 {day_total:.2f} 元")
print("欢迎光临喵喵奶茶店，祝您生活愉快！")
print("=" * 44)
