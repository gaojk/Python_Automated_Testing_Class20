# # @Time :2019/7/13 0:16
# # @Author :jinbiao


class Count:

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


if __name__ == '__main__':
    count_math = Count(2, 3)
    print(count_math.subtraction())
    print(count_math.divide())
