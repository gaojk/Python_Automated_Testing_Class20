# @Time :2019/7/9 22:44
# @Author :jinbiao


class Cat:
    kind = "猫"  # 类的属性

    def __init__(self, colour, name, age):  # 构造方法，形参接受对象的属性
        self.colour = colour    # 给对象赋值
        self.name = name
        self.age = age

    def eat(self):  # 实例方法
        cat_eat = f"{self.colour}的{self.name}{self.kind},今年{self.age}岁,吃着美味的事物"
        return cat_eat

    def drink(self):
        cat_drink = f"{self.colour}的{self.name}{Cat.kind},今年{self.age}岁,喝着可口的饮料"
        return cat_drink

    def sound(self):
        cat_eat_sound = self.eat()+"meow"+Cat.legs()    # 类内部调用实例化方法
        print(cat_eat_sound)

    @classmethod
    def legs(cls):  # 类方法
        return "猫有4只腿"


one_cat = Cat("灰色", "Tom", 1)   # 创建对象，将对象的属性传递
one_cat.eat()   # 调用对象的方法
one_cat.drink()
one_cat.sound()
print(one_cat.name)
print(Cat.kind)
print(one_cat.kind)
print(Cat.legs())
print(one_cat.legs())