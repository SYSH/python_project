#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 信号机制的使用方法

import subprocess
import signal

def sigint_handler(signum,frame):   #SIGINT信号处理函数
    print "In signal SIGINT handle"

signal.signal(signal.SIGINT,sigint_handler)   # 设置SIGINT信号处理函数


pingP = subprocess.Popen(args="ping -n4 www.sina.com.cn",shell=True)
pingP.wait()    #等待子进程完成，后面在这里会被中断
print pingP.pid
print pingP.returncode
