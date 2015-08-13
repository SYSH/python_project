#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 创建进程
'''
os模块用来创建进程，在os模块中主要包括system和exec家族函数，能够适应不同的创建进程需求
'''

# system函数用来创建进程是最快捷的方式-->函数原型： system(command)，
# 此函数表示在新进程中执行command字符串命令。如果返回值为0，则表示命令执行成功，否则表示失败

import os

print os.system("dir")   #程序最后打印出0，表示命令执行成功

'''
system函数实际上是调用系统内置的命令行程序来执行系统命令，所以在命令结束后会将控制权返回给Python进程。
exec函数有所不同，所有的exec函数在执行命令后，将会接管Python进程，而不会将控制权返回。
即：Python进程会在调用exec函数后终止；新生成的进程将会替换调用进程。这些函数都没有返回值，如果发生错误，将会触发OSError错误。
'''

