# -*- coding: UTF-8 -*-
#
#目录的创建与删除
import os

os.mkdir("hello")  # 创建
os.rmdir("hello")  # 删除
os.makedirs("hello/world")  # 创建
os.removedirs("hello/world")  # 删除

# 目录的创建三种方式:递归函数、os.path.walk()、os.walk()
import os

# 递归函数
def VisitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path,p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print pathname

if __name__ == "__main__":
    path = r"C:\Users\Rui\Desktop\filedealing"

VisitDir(path)

print '--------------------------------------------'

# os.path.walk()
import os,os.path

def VisitDir(arg,dirname,names):
    for filepath in names:
        print os.path.join(dirname,filepath)

if __name__ == "__main__":
    path = r"C:\Users\Rui\Desktop\filedealing"
    os.path.walk(path,VisitDir,())

print '---------------------------------------------'

# os.walk()
import os

def VisitDir(path):
    for root,dirs,files in os.walk(path):
        for filepath in files:
            print os.path.join(root,filepath)

if __name__ == "__main__":
    path = r"C:\Users\Rui\Desktop\filedealing"
    VisitDir(path)
