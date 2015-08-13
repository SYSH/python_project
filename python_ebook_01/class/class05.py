#! usr/bin/env python
# -*- coding: utf-8 -*-

# __init__方法：构造方法用于初始化类的内部状态

class Fruit:
    def __init__(self,color):    #初始化属性__color   构造方法
        self.__color = color
        print self.__color

    def getColor(self):
        print self.__color

    def setColor(self,color):
        self.__color = color
        print self.__color

if __name__ == "__main__":
    color = 'red'
    fruit = Fruit(color)
    fruit.getColor()
    fruit.setColor("blue")
