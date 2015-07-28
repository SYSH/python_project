# -*- coding: UTF-8 -*-
#
# stdin:流的标准输入
import sys

sys.stdin = open("hello.txt","r")
for line in sys.stdin.readlines():
    print line

# stdout:流的标准输出
import sys

sys.stdout = open(r"./hello.txt","a")
print "goodbye"
sys.stdout.close()

# stderr:用于记录输出异常信息
import sys,time

sys.stderr = open("record.log","a")
f = open(r"./hello.txt","r")
t = time.strftime("%Y-%m-%d %X",time.localtime())
context = f.read()
if context:
    sys.stderr.write(t + "" + context)
else:
    raise Exception,t + "异常信息"
