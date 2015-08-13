# -*- coding: UTF-8 -*-
#
# 文件内容的查找
import re

fl = file('hello.txt','r')
count = 0
for s in fl.readlines():
    li = re.findall('hello',s)
    if len(li) > 0:
        count = count + li.count('hello')
print "查找到" + str(count) + "个hello"
fl.close()

# 文件内容的替换
f1 = file("hello.txt",'r')
f2 = file("hello2.txt",'w')
for s in f1.readlines():
    f2.write(s.replace("hello","hi"))
f1.close()
f2.close()

print '--------------------------------------------------'

# 实现两个文件的比较
#
import difflib

f1 = file("hello.txt","r")
f2 = file("hi.txt","r")
src = f1.read()
dst = f2.read()
print src
print dst
print '--------------------------------------------------'
s = difflib.SequenceMatcher(lambda x:x == "",src,dst)
for tag,i1,i2,j1,j2 in s.get_opcodes():
    print ("% s src[%d:%d] = %s dst[%d:%d] = %s" % \
    (tag,i1,i2,src[i1:i2],j1,j2,dst[j1:j2]))
    
