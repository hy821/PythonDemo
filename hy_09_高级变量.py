# 列表(相当于数组)
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


# 遍历(iteration)
print()
for name in name_list:
    print(name)
