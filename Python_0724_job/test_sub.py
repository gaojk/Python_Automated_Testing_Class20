# @Time :2019/7/21 13:49
# @Author :jinbiao
from Python_0724_job import match_count
from Python_0724_job.operation_excel import OperationExcel
import unittest
from Python_0724_job.ddt import ddt, data
from Python_0724_job.operation_config import OperationConfig
from Python_0724_job.operation_log import log


excel_name = OperationConfig("PATH", "excelpath").get_value()
result_path = OperationConfig("PATH", "resultpath").get_value()
oe = OperationExcel(excel_name=excel_name, sheet_name="sub")
test_data = oe.get_data()


@ddt
class Testoperation(unittest.TestCase):   # 创建一个测试类，继承unitest包下的TestCase类

    @classmethod
    def setUpClass(cls) -> None:
        log.info("{:-^50}".format("测试用例开始执行"))

    @classmethod
    def tearDownClass(cls) -> None:
        log.info("{:-^50}".format("测试用例执行结果"))

    @data(*test_data)
    def test_subtraction(self, data):
        one_operation = match_count.Count(data["l_data"], data["r_data"])    # 创建一个运算对象
        actual = one_operation.subtraction()    # 调用subtraction方法，返回计算结果
        expectation = data["expect"]     # 定义期望值
        description = data["description"]
        try:
            self.assertEqual(expectation, actual, msg=f"{description}{one_operation.number1}-{one_operation.number2}不等于{expectation}")  # 判断期望值是否等于实际结果
            log.info("用例执行结果为：【PASS】")
            oe.write_data(data["case_id"] + 1, actual=actual, result="PASS")
        except Exception as e:
            log.error("用例执行结果为：【FAIL】{}\n".format(e))
            oe.write_data(data["case_id"] + 1, actual=actual, result="FAIL")
            raise e


if __name__ == '__main__':
    unittest.main()
