# -*-coding:UTF-8-*-
#
# 文件的删除操作
import os

file('hello.txt','w')
if os.path.exists('hello.txt'):
    os.remove('hello.txt')
