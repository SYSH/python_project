#! usr/bin/env python
# -*- coding: utf-8 -*-

# __new__()：在__init__()之前被调用，用于生成实例对象。利用这一特性可以实现设计模式中的单例模式 

# 单例模式只能实例化一个对象

# 实现单例模式

class Singleton(object):
    
    __intance = None           # 定义实例  私有类属性  初始值为：None

    def __init__(self):
        pass

    def __new__(cls,*args, ** kwd):         # 在__init__()之前调用
        if Singleton.__intance is None:     # 生成唯一实例 判断是否为None,如果是则调用object的__new__()方法
            Singleton.__instance = object.__new__(cls,* args,** kwd)
        return Singleton.__instance         # 返回唯一实例

    
