# -*- coding: utf-8 -*-
# 修改文件名
import os
li = os.listdir(".")
print li
if 'hello.txt' in li:
    os.rename('hello.txt','hi.txt')
elif 'hi.txt' in li:
    os.rename('hi.txt','hello.txt')

# 修改后缀名
import os

files = os.listdir(".")
for filename in files:
    pos = filename.find(".")    # 查找文件名中"."所在的位置，并赋值给pos
    if filename[pos+1:] == 'html':     # 判断后缀名是否为html，pos+1:表示“.”后位置
        newname = filename[:pos+1] + 'htm'  # 重新组合新文件名 filename[:pos+1]表示从filename的开头位置到'.'这段分片
        os.rename(filename,newname)

# 修改后缀名
import os

files = os.listdir(".")
for filename in files:
    li = os.path.splitext(filename)
    if li[1] == '.htm':
        newname = li[0] + '.html'
        os.rename(filename,newname)
