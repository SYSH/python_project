#! usr/bin/env python
# -*- coding: utf-8 -*-

# 类的方法和静态方法

class Fruit:
    price = 0                           # 公有属性

    def __init__(self):                 # 构造方法          
        self.__color = "red"            # 实例属性-->以self为前缀，只能被实例访问修改
                                        # 私有属性-->以__开头，不能被该类以外的函数调用；调用：instance._classname__attribute
    def getColor(self):                 # 该方法中有一个参数self，该参数是区分方法和函数的标志
        print self.__color              # 私有属性-->以__开头，不能被该类以外的函数调用；调用：instance._classname__attribute

    @ staticmethod                      # 静态方法-->使用staticmethod定义静态方法
    def getPrice():
        print Fruit.price

    def __getPrice():                   # 私有方法
        Fruit.price = Fruit.price + 10
        print Fruit.price

    count = staticmethod(__getPrice)     # 静态方法

    @ staticmethod                       #类方法   使用staticmethod 和self参数-->和静态方法类似
    def hasPrice(self):
        print self.price

    def __hasPrice(self):
        self.price = self.price + 10
        print self.price

    sumprice = staticmethod(__hasPrice)  #类方法


if __name__ == "__main__":
    apple = Fruit()
    apple.getColor()
    Fruit.count()
    banana = Fruit()
    Fruit.count()
    Fruit.getPrice()
    banana._Fruit__color = "green"      #私有属性的访问方式
    banana.getColor()

