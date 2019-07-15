# # @Time :2019/7/13 0:16
# # @Author :jinbiao
#
#
# 一、必做题
# 1.单元测试的作用？
# 用于测试自己所写的模块、函数、类写的是否正确，是测试断言工具
#
# 2.unittest框架中，如何测试多条用例？用例执行顺序？
# 编写多条测试用例，用例名称以test_开头
# 用例执行顺序根据测试方法名字母的ASCII码从小到大执行
#
# 3.编写如下单元测试
# 使用unittest框架来测试两数相减功能，编写用例，执行用例。
#
import unittest


class Operation:

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


class Testsubtraction(unittest.TestCase):   # 创建一个测试类，继承unitest包下的TestCase类

    def test_subtraction(self):
        one_operation = Operation(10, 2)    # 创建一个运算对象
        actual = one_operation.subtraction()    # 调用subtraction方法，返回计算结果
        expectation = 8     # 定义期望值
        self.assertEqual(expectation, actual, msg=f"{one_operation.number1}-{one_operation.number2}不等于{expectation}")  # 判断期望值是否等于实际结果


if __name__ == '__main__':
    unittest.main()

# 二、选作题
# 1.编写如下单元测试
# a.使用unittest框架来测试两数相除功能，编写用例，执行用例。
# b.使用文件来记录执行用例的结果


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

    def save_test_result(self, result):
        with open("result.txt", mode="w", encoding="utf-8") as write_file:
            write_file.write(result)


class Testdivide(unittest.TestCase):   # 创建一个测试类，继承unitest包下的TestCase类

    def test_divide(self):
        one_operation = Operation(10, 2)    # 创建一个运算对象
        actual = one_operation.divide()    # 调用divide方法，返回计算结果
        expectation = 2     # 定义期望值
        try:
            self.assertEqual(expectation, actual, msg=f"{one_operation.number1}/{one_operation.number2}不等于{expectation}")  # 判断期望值是否等于实际结果
            one_operation.save_test_result("result:SUCCESS")
        except Exception as e:
            one_operation.save_test_result("result:FAIL")
            raise e


if __name__ == '__main__':
    unittest.main()
