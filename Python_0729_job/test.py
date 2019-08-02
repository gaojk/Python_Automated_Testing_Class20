# @Time :2019/7/30 22:51
# @Author :jinbiao

import json    # 导入json模块

# 将dict数据类型转换成json格式的str类型
one_dict = {"age": 17, "sex": True, "name": None, 'hobby': "篮球"}
one_str = json.dumps(one_dict, ensure_ascii=False)
print(one_str, type(one_str))

# 将json格式的str类型数据转换成dict类型数据
two_dict = json.loads(one_str)
print(two_dict, type(two_dict))

# 将dict数据类型转换成json格式的str类型,并写入json文件
json_path = "test.txt"  # 定义文件路径
# 方法一
with open(file=json_path, mode="w", encoding="utf-8",) as write_json:
    json.dump(obj=one_dict, fp=write_json, ensure_ascii=False)
# 方法二
# json.dump(obj=one_dict, fp=open(file=json_path, mode="w"))

# 从文件中读取json格式的str类型数据，并转为dict
test = json.load(fp=open(file=json_path, encoding="utf-8"))
print(test, type(test))
