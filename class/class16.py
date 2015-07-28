#! usr/bin/env python
# -*- coding: utf-8 -*-

# 更好的继承关系:水果根据去果皮分为削皮和剥皮两类；削皮水果HuskedFruit、剥皮水果DecorticatedFruit

class Fruit:
    def __init__(self):
        pass

class HuskedFruit(Fruit):       # 削皮水果
    def __init__(self):
        print "initialize HuskedFruit"

    def husk(self):
        print "husk..."

class DecorticatedFruit(Fruit): # 剥皮水果
    def __init__(self):
        print "initialize DecorticatedFruit"

    def decorticat(self):
        print "decorticat..."

class Apple(HuskedFruit):
    pass

class Banana(DecorticatedFruit):
    pass



# 更好的继承方式：把Fruit类、HuskedFruit类、DecorticatedFruit类放在同一个层次

class Fruit(object):
    def __init__(self):
        pass

class HuskedFruit(object):       # 削皮水果
    def __init__(self):
        print "initialize HuskedFruit"

    def husk(self):              # 削皮方法
        print "husk..."

class DecorticatedFruit(object):  # 剥皮方法
    def __init__(self):
        print "initialize DecorticatedFruit"

    def decorticate(self):        # 剥皮方法
        print "decotticat..."

class Apple(HuskedFruit,Fruit):
    pass

class Banana(DecorticatedFruit,Fruit):
    pass
