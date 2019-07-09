import os
# 一、必做题
# 1. __name__变量有什么特性？
# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入

# 2.os模块中有哪些常用的方法？用什么作用？
print(os.name)  # 返回系统名称
print(os.getcwd())  # 返回当前工作目录
os.mkdir("test")   # 创建目录
# os.remove("test")  # 删除文件
os.rmdir("test")    # 删除目录
print(os.listdir())  # 列出当前目录下的所有文件
print(os.path.join("test", "test1"))
print(os.path.isfile("test"))  # 判断路径是否是文件
print(os.path.isdir("test"))    # 判断是否是目录
print(os.path.dirname(r"C:\Users\cango\PycharmProjects\Python_Automated_Testing_Class20\Python_0703_job\python_0703_homework.py"))    # 返回路径所处的目录
print(os.path.exists(r"D:\Users\cango\PycharmProjects\Python_Automated_Testing_Class20\Python_0703_job\python_0703_homework.py"))     # 判断路径是否存在

# 3.文件有哪些种类？
# 文本文件和二进制文件

# 4.文件的操作步骤
# 打开文件—读写操作—关闭文件

# 5.操作文件的常用函数/方法有哪些？
# 读取：read、readline、readlines
# 写入：write
# 关闭：close

# 6.read、readline、readlines有什么区别？
# 提示：
# 	请从返回的对象类型、应用场景来阐述
# read：读取文件中所有的内容，以字符串的格式返回
# readline: 读取整行数据,以字符串的格式返回，资源消耗低
# readlines: 读取文件中的所有内容，并以列表形式返回，可以通过列表的索引和切片返回指定行，不适用大文件

# 7. 打开文件的方式有哪些？
# 只读模式：r
# 二进制格式打开文件用于只读：rb
# 只写模式：w
# 二进制格式打开文件用于写入：wb
# 追加模式：a
# 二进制格式打开文件用于追加：ab

# 8.编写如下程序
# 将你喜欢的一首歌（音乐文件拓展名为mp3，比如刘德华忘情水.mp3），通过文件读写的方法将其复制并修改文件名

with open("忘情水.mp3", mode="rb", ) as read_mp3:
    mp3_file = read_mp3.read()

with open("忘情水copy.mp3", mode="wb") as write_mp3:
    write_mp3.write(mp3_file)

# 9.编写如下程序
# 有两行数据，存放在txt文件里面：
# url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用所学知识，读取txt文件里面的两行内容，然后转化为如下格式（嵌套字典的列表）：（可定义函数）
# [{'url':'http://test.lemonban.com/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！

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

with open("url_info.txt", mode="r") as read_file:
    file = read_file.read()
one_dict = {}
one_list = file.split("\n")
for i in one_list:
    two_list = one_list[i].split("@")
    for j in two_list:
        k, v = j.split(":", 1)
        one_dict[k] = v
        str_one = str(one_dict)
print(str_one)

# 二、选作题
# 1.编写如下程序
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

# person_info = [{"name": "可优", "age": 17, "gender": "男", "hobby": "臭美", "motto": "Always Be Coding!"},
#                {"name": "柠檬小姐姐", "age": 16, "gender": "女", "hobby": "可优", "motto": "Lemon is best!"}]
# with open("user_info.txt", encoding="utf-8", mode="r") as read_user_info:
#     user_info = read_user_info.readline().split(",")
# for i in person_info:
#     with open("user_info.txt", encoding="utf-8", mode="a") as write_user_info:
#         write_user_info.write("\n")
#         a = []
#         for j in user_info:
#             a.append(str(i[j]))
#         write_user_info.write("{}".format(",".join(a)))

