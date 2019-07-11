#
# 一、必做题
# 1.类方法、静态方法分别是什么？有作用？如何定义？
# 类方法代表整个类，传递的对象是整个类的修饰符为"@classmethod"，第一个参数为"cls"，可以操作类属性
# 静态方法是类中的一个函数和类没有直接关系，但是有间接关系。装饰器为"@staticmethod"
#
# 2.类方法、静态方法分别如何调用？
# 类方法在类内部调用：cls.类方法，对象.类方法；在类外部调用：类名.类方法，对象.类方法
# 静态方法在类内部调用：对象.静态方法，cls.静态方法；在类外部调用：类名.静态方法，对象.静态方法
#
# 3.什么是继承？有什么特性？
# 子类拥有父类的所有属性的方法，子类(父类)
#
# 4.编写如下程序
# 创建一个名为 Restaurant类，要求至少拥有饭店名和美食种类这两个特征。
# a.需要创建一个方法来描述饭店名和美食种类相关信息
# b.同时能够显示饭店营业状态（例如：正在营业）
from datetime import datetime


class Restaurant:
    def __init__(self, name, *type_food):
        self.name = name
        self.type_food = type_food

    def restaurant_info(self):
        type_foods = ",".join(self.type_food)
        print(f"{self.operating_state()}\n{self.name}欢迎您，今天的种类有{type_foods}")

    @staticmethod
    def operating_state():
        today = datetime.now().weekday()
        if today in (6, 7):
            return "今天是周末，我们任性不营业"
        else:
            return "正常营业"


if __name__ == '__main__':
    people_rest = Restaurant("上海人民饭店", *["pizza", "小龙虾"])
    people_rest.restaurant_info()


# 5.编写如下程序
# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算。

class Math:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2

    def count(self):
        print(f"加：{self.add()}\n减：{self.subtract()}\n乘：{self.multiply()}\n除：{self.divide()}")


if __name__ == '__main__':
    count = Math(1, 2)
    count.count()


# 6.将类与对象相关内容，完成思维导图
# 提示：
# 	a.此题极为重要，不做必扣分，O(∩_∩)O哈哈~
#

# 二、选作题
# 1.编写如下程序
# 编写一个工具类和工具箱类，工具需要有的名称、功能描述、价格，工具箱能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
class Tool:
    tools_kit = []  # 定义一个类属性，数据类型空列表，用来写入工具信息

    def __init__(self, name, function, price):  # 初始化工具类的属性，并赋值
        self.name = name
        self.function = function
        self.price = price


class Toolkit(Tool):    # 创建工具箱类，继承工具类

    def add_tool(self):
        """
        添加工具
        :return: 工具箱里的工具信息
        """
        self.tools_kit.append({self.name: [self.function, self.price]})
        return self.tools_kit

    def del_tool(self):
        """
        删除工具
        :return:工具箱里的工具信息
        """
        for i in self.tools_kit:
            if self.name in i.keys():
                self.tools_kit.remove(i)
        return self.tools_kit

    def query_tool(self):
        """
        查询工具箱中的工具
        :return: 工具箱里的工具信息
        """
        return self.tools_kit

    def count_tool(self):
        """
        计算工具箱中的工具个数
        :return: 工具箱里的工具个数
        """
        return len(self.tools_kit)


screwdriver = Toolkit("螺丝刀", "挤东西", "18")
print(screwdriver.add_tool())
rubberized_fabric = Toolkit("胶布", "粘东西", "2.5")
print(rubberized_fabric.add_tool())
print(screwdriver.del_tool())
print(screwdriver.query_tool())
print(screwdriver.count_tool())
