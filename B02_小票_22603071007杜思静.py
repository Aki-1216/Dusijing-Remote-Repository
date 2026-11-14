"""
实训2：项目名称-奶茶店小票生成器 (B-v2)
姓名：杜思静
学号：22603071007
班级：26数管
完成日期：2026-11-14
"""

import datetime

print("======= 欢迎使用奶茶店小票生成器 (B-v2) =======")

# 1. 基础层与挑战层：定义多种奶茶及相关信息变量（3种以上奶茶，单价、数量、折扣率等）
# 奶茶1：珍珠奶茶
name1 = "珍珠奶茶"
price1 = 15.0
qty1 = 0

# 2. 进阶层：支持第二种奶茶输入与显示
# 奶茶2：芋泥波波
name2 = "芋泥波波"
price2 = 18.0
qty2 = 0

# 奶茶3：常青款奶绿
name3 = "四季春奶绿"
price3 = 14.0
qty3 = 0

discount = 0.85  # 基础折扣率

# 2. 使用 input() 让用户输入奶茶名称、数量
print("\n【请点单】请输入您要购买的奶茶数量：")
qty1 = int(input(f"请输入 {name1}（单价 {price1} 元）的数量："))
qty2 = int(input(f"请输入 {name2}（单价 {price2} 元）的数量："))
qty3 = int(input(f"请输入 {name3}（单价 {price3} 元）的数量："))

# 获取顾客称呼（挑战层要求）
customer_name = input("请输入您的姓氏（例如：王）：")
customer_title = input("请输入您的性别/称呼（先生/女士）：")

# 获取会员身份（挑战层要求：会员再打95折）
is_member = input("是否为本店会员？(y/n)：").strip().lower()

# 3. 计算总价和折后价
subtotal1 = price1 * qty1
subtotal2 = price2 * qty2
subtotal3 = price3 * qty3
total_price = subtotal1 + subtotal2 + subtotal3  # 原总价

# 应用基础折扣
discounted_price = total_price * discount

# 如果是会员，享受额外95折（挑战层）
if is_member == 'y':
  final_price = discounted_price * 0.95
  member_str = "尊贵会员（额外95折）"
else:
  final_price = discounted_price
  member_str = "普通顾客"

# 进阶层：增加“应收金额”和“实收金额”，计算找零
receivable_amount = round(final_price, 2)
print(f"\n应收金额为: {receivable_amount:.2f} 元")
paid_amount = float(input("请输入实收现金金额: "))
change_amount = paid_amount - receivable_amount

# 获取当前日期时间（进阶层要求）
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 4. 使用 f-string 输出一张格式化小票，金额保留两位小数，价格列右对齐
print("\n" + "=" * 40)
print(f"{'*** 喵喵奶茶店结算小票 ***':^30}")
print(f"日期时间: {current_time}")
print(f"顾客: {customer_name}{customer_title} ({member_str})")
print("-" * 40)
print(f"{'商品名称':<10}{'单价':>6}{'数量':>6}{'小计':>8}")
print("-" * 40)

if qty1 > 0:
  print(f"{name1:<10}{price1:>6.2f}{qty1:>6}{subtotal1:>8.2f}")
if qty2 > 0:
  print(f"{name2:<10}{price2:>6.2f}{qty2:>6}{subtotal2:>8.2f}")
if qty3 > 0:
  print(f"{name3:<10}{price3:>6.2f}{qty3:>6}{subtotal3:>8.2f}")

print("-" * 40)
print(f"{'原价合计:':<20} ￥{total_price:>12.2f}")
print(f"{'折后应付:':<20} ￥{receivable_amount:>12.2f}")
print(f"{'实收金额:':<20} ￥{paid_amount:>12.2f}")
print(f"{'找零:':<20} ￥{change_amount:>12.2f}")
print("=" * 40)
# 挑战层：小票增加“欢迎语”
print(f"  {customer_name}{customer_title}，欢迎光临，祝您生活愉快！")
print("=" * 40)