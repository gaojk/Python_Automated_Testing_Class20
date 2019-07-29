import logging

logger = logging.getLogger(name="name")    # 创建logger日志收集器对象
logger.setLevel(level="DEBUG")    # 定义日志收集器的级别
stream = logging.StreamHandler()    # 定义日志输出渠道（控制台）
file = logging.FileHandler(filename="test.log", encoding="utf-8")   # 定义日志输出渠道（文件）
stream.setLevel(level="ERROR")
file.setLevel(level="INFO")
formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
stream.setFormatter(formater)
file.setFormatter(formater)
logger.addHandler(stream)   # 收集器添加渠道
logger.addHandler(file)
