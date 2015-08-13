#! /usr/bin/env python
# coding: utf-8

# 获取HTML资源

import urllib

# 使用urlopen打开资源，使用文件的读取函数来对数据进行操作
##r = urllib.urlopen("http://www.baidu.com")
##print r.fp.read()

fp = urllib.urlopen("http://www.baidu.com")
op = open("baidu.html","wb")

n = 0
while True:
    s = fp.read(1024)
    if not s:   # 遇到了EOF
        break
    op.write(s)
    n = n + len(s)

fp.close()
op.close()

print "retrieved",n," bytes from",fp.url


