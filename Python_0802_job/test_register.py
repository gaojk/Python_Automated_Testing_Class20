# @Time :2019/8/4 10:41
# @Author :jinbiao

from Python_0802_job.ddt import ddt, data
import unittest
from Python_0802_job.operation_log import log
from Python_0802_job import operation_config
from Python_0802_job import operation_excel
from Python_0802_job import send_request


@ddt
class TestRegister(unittest.TestCase):
    config = operation_config.do_conifg
    excel_path = config.get_value(section="PATH", option="excelpath")
    oe = operation_excel.OperationExcel(excel_path, sheet_name="register")
    test_data = oe.get_data()

    @classmethod
    def setUpClass(cls) -> None:
        log.info("{:-^50}".format("测试用例开始执行"))


    @classmethod
    def tearDownClass(cls) -> None:
        log.info("{:-^50}".format("测试用例结束执行"))

    @data(*test_data)
    def test_register(self, data):
        expect = data["expected"].replace("\n", "").replace(" ", "")
        request = send_request.SendRequest()
        actual = request.send_request(method=data["method"], url=data["url"],
                                      data=data["data"].encode("utf-8")).text
        try:
            self.assertEqual(expect, actual)
            log.info("用例执行通过")
            self.oe.write_data(row=data["case_id"]+1, actual=actual, result="PASS")
        except Exception as e:
            log.error(f"用例执行失败{e}")
            self.oe.write_data(row=data["case_id"]+1, actual=actual, result="FAIL")
            raise e


if __name__ == '__main__':
    unittest.main()

