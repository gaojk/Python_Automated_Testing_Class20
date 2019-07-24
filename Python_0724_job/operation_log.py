# @Time :2019/7/24 22:53
# @Author :jinbiao
import logging
import logging

class OperationLog:
    def __init__(self):
        self.logger = logging.getLogger("case")  # 定义日志收集器
        self.logger.setLevel(level=logging.DEBUG)    # 设置收集器的日志级别
        handler_stream = logging.StreamHandler()    # 定义日志输出渠道（控制台）
        handler_file = logging.FileHandler(filename="api_test.log", encoding="utf-8")    # 定义日志输出渠道（文件）
        handler_stream.setLevel(level=logging.ERROR)    # 定义渠道日志输出级别
        handler_file.setLevel(level=logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")    # 格式化日志
        handler_file.setFormatter(formatter)
        handler_stream.setFormatter(formatter)
        self.logger.addHandler(handler_stream)   # 收集器添加渠道
        self.logger.addHandler(handler_file)

    def get_log(self):
        return self.logger

log = OperationLog().get_log()

if __name__ == '__main__':
    OperationLog().logger.info("11111")
