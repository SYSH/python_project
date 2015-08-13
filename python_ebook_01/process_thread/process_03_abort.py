#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 终止进程

'''
当Python脚本遇到最外层的return语句而退出的时候，这个进程就终止了；另外还可以使用sys.exit和os.abort退出进程
'''
# sys.exit是一种温和退出方式，在退出前会执行一些清理操作，同时将返回值给调用进程(一般为操作系统)，通过返回值，系统知道是正常退出还是出现运行异常。
'''
下面为一个程序框架：用户调用文件名参数时，系统将打印文件名并返回"0"；否则将触发异常，并使用exit函数返回"1",
调用函数通过检查这个返回值就知道用户是否提供了参数

import sys

try:
    filename = sys.argv[1]
    print filename
except:
    print "Usage:",sys.argv[0],'filename'
    sys.exit(1)
return 0
'''

# os.abort函数
'''
os.abort函数是一种暴力退出进程的方式，将会直接给进程发生终止信号(SIGABORT信号)。在默认情况下会终止进程并不做任何清理操作；
需注意的是可以使用signal.signal()来为SIGABORT信号注册不同的信号处理函数，从而改变其默认方式
'''
# 一般在使用os.abort的地方都可也使用sys.exit替代，这样终止进程更优雅；但是在exit不能终止进程或者进程运行时间过长的情况下，可以尝试使用abort函数来解决
