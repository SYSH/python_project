#! usr/bin/env python
# -*- coding: utf-8 -*-

# 演示继承的实现

class Fruit:
    def __init__(self,color):
        self.color = color
        print "fruit's color: %s" % self.color

    def grow(self):
        print "grow..."

class Apple(Fruit):
    def __init__(self,color):
        Fruit.__init__(self,color)    # 必须显式调用父类
        print "apple's color: %s" %self.color

class Banana(Fruit):
    def __init__(self,color):
        Fruit.__init__(self,color)
        print "banana's color:%s" % self.color

    def grow(self):
        print "banana grow..."

if __name__ == "__main__":
    apple = Apple("red")
    apple.grow()
    banana = Banana("yellow")
    banana.grow()

print '-----------------------------------------------'        

# 使用super()调用父类:super类的实现继承了object,因此Fruit也必须继承object类，如果不继承,使用super会出错

class Fruit(object):
    def __init__(self):
        print "parent"

class Apple(Fruit):
    def __init__(self):
        super(Apple,self).__init__()
        print "child"

if __name__ == "__main__":
    Apple()
