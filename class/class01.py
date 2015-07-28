#! usr/bin/env python
# -*- coding: utf-8 -*-

class Fruit:
    price = 0           # 类属性-->公有属性：可以被类和实例直接调用

    def __init__(self):
        self.color = "red"    # 实例属性-->以self为前缀,只能被实例访问修改
        self.__size = "big"   # 私有属性-->以"__"开始，不能被该类以外的函数调用，访问方式：instance._classname__attribute
        zone = 'China'        # 局部变量

if __name__ == '__main__':
    print Fruit.price
    apple = Fruit()
    print apple.color
    print apple._Fruit__size
    Fruit.price = Fruit.price + 10
    print "apple's price:" + str(apple.price)

banana = Fruit()
print Fruit.price
print "banana's price:" + str(banana.price)
print banana.color
print banana._Fruit__size
