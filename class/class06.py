#! usr/bin/env python
# -*- coding: utf-8 -*-

# __del__函数：析构函数用于释放对象占用的资源

class Fruit:
    def __init__(self,color):
        self.__color = color
        print self.__color

    def __def__(self):              # 析构函数  self对于析构函数同样不可或缺
        self.__color = ""
        print "tree..."

    def grow(self):
        print "grow..."

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)           # 带参数的构造函数
    fruit.grow()                   # 执行完grow()方法后，对象fruit将超出其作用域，Python会结束对象fruit的生命周期，输出结果:tree...
    del fruit                      # 显式执行析构函数


