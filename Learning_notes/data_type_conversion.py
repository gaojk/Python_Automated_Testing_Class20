# @Time :2019/7/7 21:39
# @Author :jinbiao

"""
数据类型相互转换
"""

# python中的数据类型有int,str,list,tuple,dict,set;不能进行数据变更的类型有int,str,tuple
# [int——str]
number = 10    # 将10赋值给number，number为int类型
num_to_str = str(number)
print("number的数据类型是{},num_to_str的数据类型是{}".format(type(number), type(num_to_str)))

# [int——list]
num_to_list = []
num_to_list.append(number)
print(num_to_list)

# [str——list]
one_str = "abcdefg"
str_to_list = list(one_str)
print(str_to_list)

# 通过split分隔符进行分割，返回分割后的列表
str_to_list1 = one_str.split("d")
print(str_to_list1)

# 定义一个列表，索引或者截取想要的字符添加到列表中
str_to_list2 = [one_str[0], one_str[1]]
print(str_to_list2)

# [list——str]
# 通过字符串函数join连接列表值，但是列表值都应该为str类型
one_list = ["hello", "python", "3"]
list_to_str = "".join(one_list)
print(list_to_str)

# 通过索引列表元素再进行字符串拼接
list_to_str1 = ""
for i in one_list:
    list_to_str1 += i
print(list_to_str1)
