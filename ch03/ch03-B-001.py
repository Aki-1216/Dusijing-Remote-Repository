# ch03-B-001
# B-v3 奶茶店循环点单（基础层）
# 功能：while 循环连续点单，满减优惠，输出订单小票
# 姓名：__________  学号：__________  班级：__________  日期：__________

print("=" * 30)
print("   欢迎来到校园奶茶店")
print("=" * 30)

# 用字符串拼接保存每杯明细
receipt = ""
total = 0
count = 0

# 循环点单
while True:
    name = input("请输入奶茶名称（输入 q 结束）：")
    if name == 'q':
        break
    price = float(input("请输入单价："))
    qty = int(input("请输入数量："))
    subtotal = price * qty
    total += subtotal
    count += qty
    receipt += f"{name:<10}{price:>8.2f}{qty:>6}{subtotal:>8.2f}\n"

# 满减优惠
if total >= 80:
    discount = 15
elif total >= 50:
    discount = 8
elif total >= 30:
    discount = 3
else:
    discount = 0

final = total - discount

# 输出小票
print("\n" + "=" * 30)
print("        校园奶茶店")
print("=" * 30)
print(f"{'商品':<10}{'单价':>8}{'数量':>6}{'小计':>8}")
print("-" * 30)
print(receipt, end="")
print("-" * 30)
print(f"{'杯数：':>22}{count:>8}")
print(f"{'原价合计：':>22}{total:>8.2f}")
print(f"{'优惠金额：':>22}{discount:>8.2f}")
print(f"{'实付金额：':>22}{final:>8.2f}")
print("=" * 30)
print("        谢谢光临！")
