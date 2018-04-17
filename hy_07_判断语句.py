import random

# 随机数  1到10之前的随机数  包括 1 & 10
"""
random_num = random.randint(1,10)
print("1到10之间的随机数:%d" % random_num)
"""

"""
sechttps://www.python.org/downloads/ret = int(input("请输入6位数字密码"))

if secret > 0 and secret < 1000000 :
    print("密码格式正确")
else:
    print("密码格式不正确")
"""


# elif==else if
"""
holiday_name = "情人节"

if holiday_name == "情人节":
    print("情人节看电影")
elif holiday_name == "生日":
    print("生日吃蛋糕")
else:
    print("每天都是节日")
"""

# 逻辑判断
"""
与  and
或  or
非  not
"""

"""
is_emplee = True

if not is_emplee:
    print("不是本公司雇员")
else:
    print("是本公司雇员")
"""

# 循环
"""
i = 0;
while i < 5:
    print(i)
    i += 1
"""


# 0-100相加
"""
sum_num = 0
i = 0
max_num = 100

while i <= max_num:
    sum_num += i
    i += 1
    print("i = %d" % i)
print("Max_Num = %d" % sum_num)
"""

# 0-100 偶数相加
"""
sum_num = 0
i = 0
max_num = 100

while i <= max_num:
    if i%2 == 0:
        sum_num += i
        print("i = %d" % i)
    i += 1

print("Max_Num = %d" % sum_num)
"""

# 乘法口诀
# m = 1
# n = 1
# while m <= 9:
#     n = 1
#     while n <= m:
#         if n < m:
#             print("%dx%d=%d" % (n, m, m*n), end="\t")
#         elif n == m:
#             print("%dx%d=%d" % (n, m, m * n))
#         n += 1
#     m += 1


def multiply_table(max):
    """
    打印乘法表
    :param max: 乘法表最大数
    :return:
    """
    m = 1
    n = 1
    while m <= max:
        n = 1
        while n <= m:
            if n < m:
                print("%dx%d=%d" % (n, m, m * n), end="\t")
            elif n == m:
                print("%dx%d=%d" % (n, m, m * n))
            n += 1
        m += 1