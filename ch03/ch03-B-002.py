# ch03-B-002
# B-v3 奶茶店循环点单（进阶层）
# 功能：会员9折、杯型选择（中/大/超大）、6位随机订单编号
# 姓名：__________  学号：__________  班级：__________  日期：__________

import random

print("=" * 30)
print("   欢迎来到校园奶茶店")
print("=" * 30)

# 生成6位随机订单号
order_id = random.randint(100000, 999999)
print(f"订单编号：{order_id}")

# 会员判断
is_member = input("是否会员？（是/否）：")

receipt = ""
total = 0
count = 0

while True:
    name = input("请输入奶茶名称（输入 q 结束）：")
    if name == 'q':
        break

    # 杯型选择
    cup = input("杯型（1-中杯/2-大杯/3-超大杯）：")
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
    unit_price = price + cup_extra
    subtotal = unit_price * qty
    total += subtotal
    count += qty
    receipt += f"{name}({cup_name})".ljust(10) + f"{unit_price:>8.2f}{qty:>6}{subtotal:>8.2f}\n"

# 满减
if total >= 80:
    discount = 15
elif total >= 50:
    discount = 8
elif total >= 30:
    discount = 3
else:
    discount = 0

after_discount = total - discount

# 会员再9折
if is_member == "是":
    final = after_discount * 0.9
else:
    final = after_discount

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
if is_member == "是":
    print(f"{'会员9折：':>22}{after_discount * 0.1:>8.2f}")
print(f"{'实付金额：':>22}{final:>8.2f}")
print("=" * 30)
print("        谢谢光临！")
