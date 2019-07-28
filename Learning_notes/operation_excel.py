from configparser import ConfigParser


cp = ConfigParser()    # 创建cp对象
cp.read(filenames="config.ini", encoding="utf-8")   # 读取配置文件
value1 = cp.get(section="EXCEL", option="case_id")   # 获取配置文件的值
value2 = cp["EXCEL"]["method"]
print(value1, value2)


one_dict = {"EXCEL": {"case_id": 1, "request_url": "www.baidu.com", "method": "post"}}    # 定义一个嵌套字典的字典
for data in one_dict:   # 循环字典，将字典的键值传给配置文件，并写入
    cp[data] = one_dict[data]
    with open(file="config2.ini", mode="w", encoding="utf-8") as write_conf:
        cp.write(fp=write_conf)
