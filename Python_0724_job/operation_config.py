from configparser import ConfigParser


class OperationConfig:
    """
    操作配置文件
    """
    def __init__(self, filename, section=None, option=None):
        """
        构造方法，初始化实例属性
        :param filename: 配置文件路径
        :param section: 区域名
        :param option: 选项名
        """
        self.filename = filename
        self.section = section
        self.option = option
        self.cp = ConfigParser()
        self.cp.read(filename, encoding="utf-8")

    def get_value(self):
        return self.cp.get(section=self.section, option=self.option)

    def get_int_value(self):
        return self.cp.getint(section=self.section, option=self.option)

    def get_float_value(self):
        return self.cp.getfloat(section=self.section, option=self.option)

    def get_bool_value(self):
        return self.cp.getboolean(section=self.section, option=self.option)

    def get_eval_value(self):
        return eval(self.cp.get(section=self.section, option=self.option))

    @staticmethod
    def write_config(filename, datas):
        """
        写入配置文件
        :param filename: 配置文件
        :return: None
        """
        cp = ConfigParser()
        if isinstance(datas, dict):
            for key in datas:
                if not isinstance(datas[key], dict):
                    return "配置文件数据格式错误"
                cp[key] = datas[key]
            with open(file=filename, mode="w") as write_config:
                cp.write(write_config)
        else:
            print("配置文件数据格式错误")


if __name__ == '__main__':
    op = OperationConfig(filename="config.ini", section="EXCEL", option="l_data")
    print(op.get_value())
    config_data = {"EXCEL": {"case_id": 1}, "PATH": {"excelpath": "test_data.xlsx"}}
    op.write_config(filename="test.ini", datas=config_data)
