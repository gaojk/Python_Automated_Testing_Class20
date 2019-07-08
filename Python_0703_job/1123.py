# @Time :2019/6/18 23:11
# @Author :jinbiao
# price = float(input("收银员输入橘子的价格，单位：元／斤"))
# weight = float(input("收银员输入用户购买橘子的重量，单位：斤"))
# sum_price = price * weight
# print(type(sum_price))
# print("您需要支付的金额为{:.2f}".format(sum_price))
# name = input("请输入您的姓名")
# age = input("请输入您的年龄")
# sex = input("请输入您的性别")
# hobby = input("请输入您的爱好")
# screen_name = input("请输入您的网名")
# motto = input("请输入您的座右铭")
# print(("*" * 20 + "\n个人信息展示\n{}({})\n年龄:{}\n性别:{}\n爱好:{}\n座右铭:{}\n" + "*" * 20).format(name, screen_name, age, sex, hobby, motto))

# number = int(input("请输入1-7中数字"))
# if number in (6, 7):
#     print("周末")

# list1 = ["周末", "无聊", "coding"]
# list2 = ["LOL", "王者荣耀"]
# list1.extend(list2)
# print(list1)

# keyou_info = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# index = keyou_info.index("矮穷丑")
# del keyou_info[index]
# #keyou_info.pop(index)
# keyou_info.remove("矮穷丑")
# print(keyou_info)

# per_info = {"姓名": "前额有个旋", "性别": "男", "年龄": "90", "身高": 183}
# other_info = {"性格": "活泼", "爱好": "篮球", "座右铭": "每天比昨天进步一点"}
# dict1 = dict(per_info, **other_info)
# print(dict1)
# #修改年龄
# per_info["年龄"] = 18
# print(per_info)
# #获取字典中年龄的值
# print(dict1["年龄"])

# list1 = [1, "wode"]
# list1.insert(0, "women")
# print(list1)
# del_value = list1.pop(1)
# print(del_value)
# list1.remove("women")
# print(list1)
# del list1[0]
# print(list1)
# list1.clear()
# print(list1)

# tuple1 = ("abc", 2)
# print(tuple1)
# del tuple[0]
# print(tuple1)

# str1 = '我是很多个字符组成的字符串'
# # print(str1[3::2])

# dict1 = {1: "周一", 2: "周二"}
# print(dict1.keys(), type(dict1.keys()))
# print(list(dict1.keys()))

# a = [1, 2, 3, "this is a list"]
# b = [4, 5, 6, "这是第二个列表"]
# a = a+b
# print(a[0])
# print(a[2:4])
# print(a[3:-1])

# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

# a = 100
# b = 200
# # 通过第三个变量进行中转
# c = a
# a = b
# b = c
# print(a, b)
#
# # 直接赋值
# a, b = b, a
# print(a, b)


# def chang_variable(a=100, b=200):
#     """
#     更换变量值
#     :param a:变量a
#     :param b:变量b
#     :return:
#     """
#     return a, b
#
#
# print(chang_variable(200, 100))
# print("a:{}\tb:{}".format(a, b))


# def int_maping_str():
#     """
#     数字字符映射
#     :return: 返回对应的字符
#     """
#     num_str_dic = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
#     while True:
#         number = int(input("请输入0-9之间的数字"))
#         if number in range(10):
#             output = num_str_dic[str(number)]
#             break
#         else:
#             print("输入有误，请重新输入")
#     return output
#
#
# output_str = int_maping_str()
# print(output_str)


# def login(user_name, password):
#     """
#     登录判断，判断用户名密码是否正确
#     :param user_name: 用户输入的用户名
#     :param password:用户输入的密码
#     :return:返回是否正确
#     """
#     if user_name == "lemon" and password == "best":
#         back = "登录成功"
#     else:
#         back = "用户名或密码错误"
#     return back
#
#
# while True:
#     user_name = input("请输入您的用户名")
#     password = input("请输入您的密码")
#     back_value = login(user_name, password)
#     print(back_value)
#     if back_value == "用户名或密码错误":
#         pass
#     else:
#         break


# def number_mul(*args):
#     result = 1
#     for i in args:
#         result *= int(i)
#     result = result % 20
#     return result
#
#
# number = tuple(input("请输入数字").split(","))
# print("余数为{}".format(number_mul(*number)))

# import math
#
#
# def count_area(radius):
#     area = math.pi * radius**2
#     return area
#
#
# radius = float(input("请输入圆的半径"))
# print("圆的体积为:{:.2f}".format(count_area(radius)))

import random


# def morra(gesture):
#     dict1 = {1: "石头", 2: "剪刀", 3: "布"}
#     user = list(dict1.keys())[list(dict1.values()).index(gesture)]
#     computer = random.randint(1, 3)
#     print("电脑出的是{:s}".format(dict1[computer]))
#     print("用户处的是{:s}".format(gesture))
#     if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and user == 1):
#         result = "用户胜利"
#     elif user == computer:
#         result = "平手"
#     else:
#         result = "电脑胜利"
#     return result
#
#
# gesture = input("请猜拳")
# print(morra(gesture))
#
#
# def number_mul(*args, **kwargs):
#     result = 1
#     for i in args:
#         result *= int(i)
#
#     for i in list(kwargs.values()):
#         result *= i
#     result = result % 20
#     return result
#
#
# user_input = (input("请输入"))
# one_list = user_input.split("=")
# print(one_list)
# print("余数为{}".format(number_mul(1, 7, 3, a=7, b=5)))


# import module_20190702.design_formulas as des
# from module_20190702.design_formulas import *
# from module_20190702.design_formulas import pebrach_sequence

# 输入长方形的长度和宽度
# length = float(input("请输入长方形的长度"))
# width = float(input("请输入长方形的宽度"))
# # 计算长方形的面积
# print("长方形的长度为{:.2f};宽度为{:.2f};长方形面积为:{:.2f}".format(length, width, des.area_of_rectangle(length, width)))
# # 计算长方形的周长
# print("长方形的长度为{:.2f};宽度为{:.2f};长方形周长为:{:.2f}".format(length, width, perimeter_of_rectangle(length, width)))
#
# # 输入圆的半径
# radius = float(input("请输入圆的半径"))
# print("圆的半径为{:.2f};圆的面积为{:.2f}".format(radius, area_of_circle(radius)))
# print("圆的半径为{:.2f};圆的周长为{:.2f}".format(radius, circumference(radius*2)))

# 计算小于用户输入数值的裴伯拉切数列
# number = int(input("请输入正整数"))
# print("小于{}的裴伯拉切数列有{}".format(number, pebrach_sequence(number)))


# 套餐满20免米饭费
# ten_cai = ["鸡腿", "鱼肉", "大排", "酸菜鱼"]
# six_cai = ["西红柿炒鸡蛋", "木耳炒肉", "白菜炒肉", "豇豆炒肉"]
# four_cai = ["白菜", "海带丝", "凉拌黄瓜", "青菜"]
# rice = 2
#
# taocan = input("请输入你要的菜品").split(",")
# price = 0
# for i in taocan:
#     if i in ten_cai:
#         print(i)
#         price += 12
#     elif i in six_cai:
#         print(i)
#         price += 6
#     else:
#         print(i)
#         price += 4
# if price < 20:
#     price = price + rice
# print(price)


# with open("url_info.txt", mode="r") as read_file:
#     file = read_file.read()
# one_dict = {}
# two_dict = {}
# one_list = file.split("\n")
# two_list = one_list[0].split("@")
# for j in two_list:
#     k, v = j.split(":", 1)
#     one_dict[k] = v
# three_list = one_list[1].split("@")
# for j in three_list:
#     k, v = j.split(":", 1)
#     two_dict[k] = v
# four_list = [one_dict, two_dict]
# print(four_list)

# 将你喜欢的一首歌（音乐文件拓展名为mp3，比如刘德华忘情水.mp3），通过文件读写的方法将其复制并修改文件名
# with open("忘情水.mp3", mode="rb", ) as read_mp3:
#     mp3_file = read_mp3.read()
#
# with open("忘情水copy.mp3", mode="wb") as write_mp3:
#     write_mp3.write(mp3_file)


# 创建一个txt文本文件，以csv格式（数据之间以英文逗号分隔）来添加数据
# a.第一行添加如下内容：
# name,age,gender,hobby,motto
# b.从第二行开始，每行添加具体信息，例如：
# 可优,17,男,臭美,Always Be Coding!
# 柠檬小姐姐,16,女,可优,Lemon is best!
# c.具体用户信息要求来自于一个嵌套字典的列表（请自定义这个列表），例如：
# person_info = [{"name": "可优",
#                "age": 17,
#                "gender": "男",
#                "hobby": "臭美",
#                "motto": "Always Be Coding!"},
#               {"name": "柠檬小姐姐",
#                "age": 16,
#                "gender": "女",
#                "hobby": "可优",
#                "motto": "Lemon is best!"},
#               ]
# d.将所有用户信息写入到txt文件中之后，然后再读出
# e.有精力的同学可以试试，多种方法来读取文件，比如csv模块（不作要求）
# 注意：csv格式的数据，是以英文逗号分隔的




person_info = [{"name": "可优","age": 17,"gender": "男","hobby": "臭美","motto": "Always Be Coding!"},{"name": "柠檬小姐姐","age": 16,"gender": "女","hobby": "可优","motto": "Lemon is best!"}]
with open("user_info.txt", encoding="utf-8", mode="r") as read_user_info:
    user_info = read_user_info.readline().split(",")
for i in person_info:
    with open("user_info.txt", encoding="utf-8", mode="a") as write_user_info:
        write_user_info.write("\n")
        a = []
        for j in user_info:
            a.append(str(i[j]))
        write_user_info.write("{}".format(",".join(a)))


