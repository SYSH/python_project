#! usr/bin/env python
# -*- coding: utf-8 -*-

# 多重继承

class Fruit(object):
    def __init__(self):
        print "initialize Fruit"

    def grow(self):
        print "grow..."

class Vegetable(object):
    def __init__(self):
        print "initialize Vegetable"

    def plant(self):
        print "plant..."

class Watermelon(Vegetable,Fruit):      # 多重继承,但是Watermelon只会调用第一个被继承的类的__init__()
    pass 

if __name__ == "__main__":
    w = Watermelon()
    w.grow()
    w.plant()
