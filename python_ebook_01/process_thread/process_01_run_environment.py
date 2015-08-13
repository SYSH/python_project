#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
os模块中提供了environ属性，用来记录当前进程的运行环境。为字典型数据结构：键（key）为环境变量的名，
值（value）为环境变量的值。环境变量的名一般全部用大写。

'''

import os

# 获取当前环境变量中PATH值
path = os.environ.get("PATH")
print path

# 输出当前进程中所有环境变量的值
for key in os.environ.keys():
    print key,"-->",os.environ[key]

# 修改或添加环境变量，此环境变量仅对当前的进程有效，若希望起全局作用，必须将其写入系统配置中

# os.environ['key'] = 'value'

