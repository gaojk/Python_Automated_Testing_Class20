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