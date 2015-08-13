#! /usr/bin/env python
# -*- coding: utf-8 -*-

t = ('hello',)
assert len(t) >= 1
t = ("hello")         
##assert len(t)==1     # assert语句断言失败，会引发AssertionError异常


# 带message的assert语句

month = 13
assert 1 <= month <= 12,"month errors"
