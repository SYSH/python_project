#! urs/bin/env python
# -*- coding: utf-8 -*-

# 动态添加类的方法

class Fruit:
    pass

def add(self):
    print "grow..."

if __name__ == "__main__":
    Fruit.grow = add
    fruit = Fruit()
    fruit.grow()


# 动态更新方法,对已经定义的方法进行修改

class Fruit:
    def grow(self):
        print "grow..."

def update():
    print "new grow......"

if __name__ == "__main__":
    fruit = Fruit()
    fruit.grow()
    fruit.grow = update
    fruit.grow()
