import unittest
from Python_0802_job import HTMLTestRunnerNew
from datetime import datetime
import os

# 创建测试套件对象
one_suite = unittest.TestSuite()
# 创建测试加载器对象
one_loader = unittest.TestLoader()
# 将测试用例添加到测试套件
# one_suite.addTest(one_loader.loadTestsFromModule(python_0712_homework))
one_suite.addTest(one_loader.discover(start_dir=".", pattern="test*"))
# 创建执行器对象
if not os.path.exists("test_reports"):
    os.mkdir("test_reports")

current_time = f"{datetime.now():%Y%m%d%H%M%S}"+".html"
with open(f"test_reports/report_{current_time}", mode="wb") as write_report:
    one_runner = HTMLTestRunnerNew.HTMLTestRunner(stream=write_report, verbosity=2, title="测试报告", description="副标题", tester="jinbiao")
    one_runner.run(one_suite)

