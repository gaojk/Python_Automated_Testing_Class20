# @Time :2019/7/11 22:51
# @Author :jinbiao

# 字符串内建函数练习
# 字符串是不可变类型，所以原字符串始终未变
one_str = "   我是字符串类型的数据类型   "
print(len(one_str))     # 字符串长度
print(one_str.split("类", 1))   # 字符串分割，返回分割列表
print(one_str.strip())  # 清空字符串左右两侧的空格
print(one_str.replace("我", "你"))    # 字符串数据替换
two_str = "123456 "
print(two_str.isdigit())   # 判断是否只包含数字
three_str = "abcdef"
print(three_str.isalnum())  # 判断字母或数字
print(three_str.isalpha())  # 判断都是字母
print(three_str.islower())  # 判断都是小写
print(three_str.isupper())    # 判断都是大写
print(three_str.istitle())  # 判断是否为标题
print(three_str.startswith("a"))    # 判断首字母
print(three_str.endswith("a"))  # 判断尾字母
one_list = ["1", "2", "3", "4", "5"]
print("*".join(one_list))   # 用字符串拼接列表元素，列表元素为字符串
print(three_str.index("a"))     # 索引字符串的位置，找不到抛异常
print(three_str.find("a"))  # 所有字符串的位置，还有左右开始索引，找不到返回-1
print(three_str.upper())    # 字母大写
print(three_str.lower())    # 字母小写
print(three_str.center(50, "*"))    # 居中对齐
print(three_str.count("a"))     # 计算某个字符串的次数
print(three_str.title())    # 字符串标题化
print(min(three_str))   # 返回最小的字母
print(max(three_str))   # 返回最大的字母

