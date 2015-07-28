#! usr/bin/env python
# -*- coding: utf-8 -*-

# 多态性

class Fruit:
    def __init__(self,color = None):
        self.color = color

class Apple(Fruit):
    def __init__(self,color = "red"):
        Fruit.__init__(self,color)

class Banana(Fruit):
    def __init__(self,color = "yellow"):
        Fruit.__init__(self,color)

class FruitShop:
    def sellFruit(self,fruit):       # 参数fruit接收Apple、Banana类的实现
        if isinstance(fruit,Apple):  # 分别判断参数fruit的类型，是否为Apple 
            print "sell apple"
        if isinstance(fruit,Banana): # 是否为Banana 
            print "sell banana"
        if isinstance(fruit,Fruit):  # 是否为Fruit
            print "sell fruit"

if __name__ == "__main__":
    shop = FruitShop()
    apple = Apple("red")
    banana = Banana("yellow")
    shop.sellFruit(apple)       # 参数的多态性，传递apple对象
    shop.sellFruit(banana)      # 参数的多态性，传递banana对象
