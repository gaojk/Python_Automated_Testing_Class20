# @Time :2019/7/6 7:51
# @Author :jinbiao

# 一、必做题
# 1.什么是异常？为什么要捕获异常？

# 异常就是程序在运行时发生的错误
# 可以在程序抛出异常后不终止程序，增加程序的容错性

# 2.异常的完整语法格式

try:
    pass    # 可能出现异常的代码块，异常在此抛出
except:  # 捕获异常,可指定异常类型
    pass    # 成功捕获后执行的代码块

# 3.在异常中，try关键字下的块语句、except下的块语句、else下的块语句、finally下的块语句执行逻辑是什么？

try:
    pass    # 如果出现错误，将会抛出异常
except:
    pass    # 捕获异常后，执行except下的代码块
else:
    pass    # 没有抛出异常时，执行else下的代码块
finally:    # 无论有没有抛出异常，都会执行finally下的代码块
    pass

# 4.编写如下程序
# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况。


# def count_price(unit_price, weight):
#     total_price = unit_price * weight
#     return total_price
#
#
# while True:
#     try:
#         unit_price = float(input("请输入橘子的单价"))
#         weight = float(input("请输入橘子的重量"))
#     except Exception:
#         print("请输入正确的格式")
#     else:
#         a = count_price(unit_price=unit_price, weight=weight)
#         print(a)
#         break

# 5.编写如下程序
# 优化剪刀石头布优秀程序
# a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# b.电脑随机出拳
# c.比较胜负，显示用户胜、负还是平局
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
# f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况
# h.如果使用文件保存用户历史胜负数据，需要使用异常来处理文件不存在的情况（选做）

import random


with open("game_file.txt", mode="r", encoding="utf8") as read_game_file:
    game_data = read_game_file.read()
    if len(game_data) > 0:
        data_list = game_data.split(",")
        win_count, lose_count, draw_count = int(data_list[1]), int(data_list[2]), int(data_list[3])
    else:
        win_count, lose_count, draw_count = 0, 0, 0
# 猜拳判断
def morra(gesture):
    """
    猜拳结果逻辑判断
    :param gesture: 用户出的什么
    :return: 结果和次数
    """
    global win_count, lose_count, draw_count
    dict1 = {1: "石头", 2: "剪刀", 3: "布"}
    user = list(dict1.keys())[list(dict1.values()).index(gesture)]
    computer = random.randint(1, 3)
    print("电脑出的是{:s}".format(dict1[computer]))
    print("用户出的是{:s}".format(gesture))
    if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and user == 1):
        result = "你赢啦"
        win_count += 1
    elif user == computer:
        result = "你们实力相当，平手啦"
        draw_count += 1
    else:
        result = "你输啦"
        lose_count += 1
    return result, win_count, lose_count, draw_count

# 退出游戏存档
def on_file(*args):
    """
    将游戏结果数据保存到txt文件中，方便下次读取
    :param args: 游戏数据
    :return: None
    """
    with open("game_file.txt", mode="w", encoding="utf8") as write_game_file:
        for i in args:
            write_game_file.write(str(i)+",")


# 用户进行猜拳游戏
with open("game_file.txt", mode="r", encoding="utf8") as read_game_file:
    a = read_game_file.read()
    if len(a) >0:
        data_list = a.split(",")
        print("您的历史战绩为赢{}次，输{}次,平{}次".format(data_list[1], data_list[2], data_list[3]))
while True:
    try:
        gesture = str(input("请猜拳"))
        onelist = morra(gesture)
        print(onelist[0])
        quit_game = str(input("是否退出游戏"))
        if quit_game == "是":
            print("本次游戏结束，你战绩为：赢{}次,输{}次，平{}次".format(onelist[1], onelist[2], onelist[3]))
            on_file(*onelist)
            break
    except Exception as e:
        print("输入有误，请重新输入"+e)

