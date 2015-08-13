#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 使用subprocess模块中的Popen类管理进程

import subprocess

pingP = subprocess.Popen(args='ping -c4 www.baidu.com',shell=True,stdout = subprocess.PIPE)   #生成ping进程
pingP.wait()       # 等待进程完成
print pingP.pid    # 打印进程ID
print pingP.returncode   # 打印进程返回值
