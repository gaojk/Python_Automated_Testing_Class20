# 1.使用测试套件批量执行用例的顺序是？
# 如果是按照模块导入的方式将测试用例添加测试套件，执行顺序为添加先后顺序
# 如果是按照discover的方式将测试用例添加到测试套件，是按照ASCII码顺序从小到大执行的
#
# 2.将用例加载到测试套件中，有哪几种方式？
import unittest
# unittest.defaultTestLoader.discover()   # 加载路径下所有以test开头的测试用例
# unittest.TestLoader.loadTestsFromModule()   # 加载想要测试的模块下的测试用例

# 3.编写如下单元测试
# 将上一次作业中的两数相减测试类与两数相除测试类的所有用例，使用测试套件来批量执行
# 提示：
# 	a.需要使用日志文件，来记录用例执行日志


from Python_0717_job import python_0712_homework
from HTMLTestRunnerNew import HTMLTestRunner
import time
import os

# 创建测试套件对象
one_suite = unittest.TestSuite()
# 创建测试加载器对象
one_loader = unittest.TestLoader()
# 将测试用例添加到测试套件
one_suite.addTest(one_loader.loadTestsFromModule(python_0712_homework))
# one_suite.addTest(one_loader.discover(start_dir=".", pattern="python*"))
# 创建执行器对象
# one_runner = unittest.TextTestRunner()
if not os.path.exists("test_reports"):  # 判断目录是否存在，不存在创建测试报告存放目录
    os.mkdir("test_reports")

current_time = time.strftime("%Y-%m-%d", time.localtime())  # 获取当前时间并格式化
with open("test_reports/report{}.html".format(current_time), mode="wb") as write_report:
    one_runner = HTMLTestRunner(stream=write_report, verbosity=2, title="测试报告", description="11111111", tester="jinbiao")
    one_runner.run(one_suite)
