#! usr/bin/env python
# -*- coding: utf-8 -*-

# __getattr__()/__getattribute__()/__setattr__()：属性获取和设置方法

class Fruit(object):
    def __init__(self,color = "red",price = 0):
        self.__color = color
        self.__price = price

    def __getattribute__(self,name):                # 获取属性的方法
        return object.__getattribute__(self,name)

    def __setattr__(self,name,value):               # 设置属性的方法
        self.__dict__[name] = value

    
if __name__ == "__main__":
    fruit = Fruit("blue",10)
    print fruit.__dict__.get("_Fruit__color")       # 获取color属性
    fruit.__dict__["_Fruit__price"] = 5             # 设置price属性
    print fruit.__dict__.get("_Fruit__price")
