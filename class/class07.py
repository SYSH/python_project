#! usr/bin/env python
# -*- coding: utf-8 -*-

# 使用gc模块显示的调用垃圾回收机制

import gc

class Fruit:
    def __init__(self,name,color):      # 初始化name,color属性
        self.__name = name
        self.__color = color

    def getColor(self):
        print self.__color

    def setColor(self,color):
        self.__color = color

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

class FruitShop:
    def __init__(self):              # 这是个列表，用于存放水果店中的水果
        self.fruits=[]  

    def addFruit(self,fruit):
        fruit.parent = self         # 设置fruit对象的parent属性为self
        self.fruits.append(fruit)   # 即把FruitShop实例化对象的引用关联到添加的fruit对象上

if __name__ == "__main__":
    shop = FruitShop()
    shop.addFruit(Fruit("apple","red"))
    shop.addFruit(Fruit("banana","yellow"))
    print gc.get_referrers(shop)
    del shop
    print gc.collect()
        
