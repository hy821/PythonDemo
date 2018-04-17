# 列表(相当于数组)-----------------------------------
name_list = ["张三", "李四", "王五"]
# 取值 取索引
print(name_list[1])
print(name_list.index("王五"))

# 修改
name_list[1] = "修改李四"
print(name_list)

# 增加 三种形式
name_list.append("赵六")          # 末尾追加
print(name_list)

name_list.insert(1,"插入到索引1")  # 插入到指定索引位置
print(name_list)

temp_list = ["a","b","c"]
name_list.extend(temp_list)               # 把其他列表加入
print(name_list)


# 删除 三种形式
name_list = ["张三", "李四", "王五", "a", "b", "c"]
name_list.remove("王五")  # 移除指定数据
print(name_list)

name_list.pop()  # pop 默认移除列表最后一个元素
print(name_list)

name_list.pop(1)  # 移除指定索引元素
print(name_list)

name_list.clear()  # 清空列表

# 特殊删除  del 是把一个变量从内存中删除 后续代码不可使用删掉的变量了
# del name_list[1]   # 也可以删除数据, 但是不建议使用, 使用列表的删除方法

# 列表中元素总数
name_list = ["1", "2", "3", "4", "5", "4", "3"]
list_len = len(name_list)
print(list_len)

# 列表中某个元素总个数
four_count = name_list.count("4")
print(four_count)

# 从列表中删除数据 假设这个数据有多个 删除的是第一次出现的数据--->第一个4
name_list.remove("4")
print(name_list)


# 排序
name_list = ["abb", "cdd", "wangwu", "zhaoliu", "wangxiaoer"]
num_list = [10, 21, 3, 4, 5, 5]

# 升序排序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)

# 降序排序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)

# 逆序(反序)    把元素反过来  比如 3 2 5 6   逆序  6 5 2 3
name_list.reverse()
num_list.reverse()


# 迭代遍历 (迭代iteration)
"""
顺序的从列表中获取数据
"""
print()
for name in name_list:
    print("迭代遍历:%s" % name, end=" ")





# 元祖(Tuple)和列表很相似, 差别: 一旦定义完成, 不能修改内部数据
"""
元祖用于存储一串信息,数据. 
用()定义, 数据用","隔开
"""
# 创建空元祖 很少创建空元组, 因为一旦定义完成, 不能修改.
empty_tuple = ()

# 创建只包含一个元素的元祖, 需要在元素后面加逗号","
single_tuple = (5,)    # single_tuple = (5)   这是一个int类型的simgle_tuple

# 元祖
normal_tuple = ("小明", 18, 175, 18)

# 元祖常用操作
# 1,取值and取索引
print("\n\n名字叫%s" % normal_tuple[0])
print("名字索引数:%s" % normal_tuple.index("小明"))

# 2,统计计数 & 元祖中包含元素总个数
print("18的出现次数:%s" % normal_tuple.count(18))
print("元祖元素总个数:%s" % len(normal_tuple))

""" 
元祖的遍历
可以使用for循环遍历所有非数字型类型的变量: 列表,元祖,字典,字符串
在实际开发中, 除非明确知道元祖内元素类型, 一般很少遍历元祖
"""

""" 元祖应用场景: 
1, 作为函数的参数,返回值, 这样一个元素就可以传任意多个参数,或者一次返回多个返回值
2, 格式字符串, 格式字符串后面的() 本质上就是元祖    举例如下
3, 让列表不被修改, 保护数据安全
"""
print("%s的年龄%d岁,身高%.2f米" % ("小明", 18, 1.75))
str_tuple = ("小明", 18, 1.75)
print("%s的年龄%d岁,身高%.2f米" % str_tuple)


# 元祖和列表的互相转换 比如想修改元祖内容, 可以先转出列表,   或者把列表转成元祖,保护数据内容
a_list = [1, 2, 3]
a_tuple = ("A", 2, 3)

print(list(a_tuple))
print(tuple(a_list))



# 字典
"""
字典无序, 字典的键:只能是字符串,数字,元祖, 值可以是任何数据类型
"""
msg_dic = {"name": "XiaoMing",
           "age": 18,
           "sex": "男",
           "Height": 175
           }

# 删除键值对  pop(key)  如果删除的key不存在, 会报错
msg_dic.pop("name")
print(msg_dic)

# 1,统计键值对数量
print(len(msg_dic))

# 2,合并字典  如果被合并的字典里包含已有键值, 原字典里的键值会被覆盖
temp_dic = {"name": "小小明",
            "age": 28,
            "address": "上海市"
            }

msg_dic.update(temp_dic)

print(msg_dic)

# 遍历 遍历字典的需求不多,因为字典里的键对应的值的类型不同
for k in msg_dic:
    print(k, msg_dic[k])



# 字符串 可以用" 也可以用'定义
"""
字符串内部使用双引号时, 用'来定义   
字符串内部使用单引号时, 用"来定义
也可以用 \"  \' 来实现
"""
str = '我的外号叫"大西瓜"'
str1 = "我的外号叫'大西瓜'"
print(str)
print(str1)

# 字符串也可以遍历

for char in str:
    print(char,end=" ")


llist = str.split("\"")
print("list:%s" % llist)

