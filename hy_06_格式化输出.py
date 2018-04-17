
# input("提示语相当于placeholder") 得到的一定是字符串 可以通过转换得到整数or浮点数
# 类型转换 int(x) 转整数   float(y) 转浮点数

price = float(input("苹果单价:"))
weight = float(input("苹果重量:"))

# 格式化输出
print("苹果单价:%.2f元" % price)
print("苹果单价:%.2f元, 苹果重量:%.0f斤, 苹果总价:%.2f元" % (price, weight, price*weight))


