#! usr/bin/env python
# -*- coding: utf-8 -*-

# 实现运算符 << 的重载

import sys

class Stream:
    def __init__(self,file):
        self.file = file

    def __lshift__(self,obj):       # 对运算符<<进行重载
        self.file.write(str(obj))
        return self

class Fruit(Stream):
    def __init__(self,price = 0,file = None):
        Stream.__init__(self,file)
        self.price = price

class Apple(Fruit):
    pass

class Banana(Fruit):
    pass


if __name__ == "__main__":
    apple = Apple(2,sys.stdout)     # apple对象可作为流输出,输出结果到控制台
    banana = Banana(3,sys.stdout)
    endl = "\n"
    apple << apple.price << endl
    banana << banana.price << endl
