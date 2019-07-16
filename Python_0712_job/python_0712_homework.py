# # @Time :2019/7/13 0:16
# # @Author :jinbiao

import unittest


class Sub:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def subtraction(self):
        """
        计算两个数值相减
        :return: 计算结果
        """
        value = self.number1 - self.number2
        return value


class Operation:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def divide(self):
        """
        计算两个数相除
        :return: 相除的结果
        """
        try:
            value = round(self.number1 / self.number2, 2)
            return value
        except ZeroDivisionError:
            return "分母不能为0"


class Testoperation(unittest.TestCase):   # 创建一个测试类，继承unitest包下的TestCase类

    @classmethod
    def setUpClass(cls) -> None:
        cls.write_file = open("result.txt", mode="a", encoding="utf-8")
        cls.write_file.write("{:#^50}\n".format("测试用例开始执行"))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.write_file.write("{:#^50}".format("测试用例执行结果"))
        cls.write_file.close()

    def test_divide(self):
        one_operation = Operation(10, 2)    # 创建一个运算对象
        actual = one_operation.divide()    # 调用divide方法，返回计算结果
        expectation = 2     # 定义期望值
        try:
            self.assertEqual(expectation, actual, msg=f"{one_operation.number1}/{one_operation.number2}不等于{expectation}")  # 判断期望值是否等于实际结果
            self.write_file.write("用例执行结果为：【PASS】\n")
        except Exception as e:
            self.write_file.write("用例执行结果为：【FAIL】{}\n".format(e))
            raise e

    def test_subtraction(self):
        one_operation = Sub(10, 2)    # 创建一个运算对象
        actual = one_operation.subtraction()    # 调用subtraction方法，返回计算结果
        expectation = 8     # 定义期望值
        try:
            self.assertEqual(expectation, actual, msg=f"{one_operation.number1}-{one_operation.number2}不等于{expectation}")  # 判断期望值是否等于实际结果
        except Exception as e:
            self.write_file.write("用例执行结果为：【FAIL】{}\n".format(e))
            raise e


if __name__ == '__main__':
    unittest.main()
