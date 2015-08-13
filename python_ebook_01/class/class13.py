#! usr/bin/env python
# -*- coding: utf-8 -*-

# 模拟抽象类的实现

def abstract():
    raise NotImplementedError("abstract")

class Fruit:
    def __init__(self):
        if self.__class__ is Fruit:  # 如果实例化的类是Fruit,则抛出异常
            abstract()
        print "Fruit"

class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)         # 调用父类的__init__()
        print "Apple"
    
if __name__ == "__main__":
    apple = Apple()      # Apple是继承了Fruit，所以不会抛出异常
    fruit = Fruit()      # 对Fruit类进行实例化，则会抛出异常
