# -*- coding: UTF-8 -*-
#
# 目录的遍历三种方式：递归函数、os.path.walk()、os.walk()

# 递归函数
import os
def VisitDir(path):
    li = os.listdir(path)  # 返回一个无序的列表，该列表包含给定path路径中所有目录项的名称
    for p in li:
        pathname = os.path.join(path,p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print pathname
    
if __name__ == "__main__":
    path = r"E:\python_project\trunk\filedealing"
VisitDir(path)

print '-----------------------------------------------------'

# os.path.walk()

import os,os.path

def VisitDir(arg,dirname,names):
    for filepath in names:
        print os.path.join(dirname,filepath)

if __name__ == "__main__":
    path = r"E:\python_project\trunk\filedealing"
    os.path.walk(path,VisitDir,())

print '-----------------------------------------------------'

# os.walk()  效率比  os.path.walk()高

import os,os.path

def VisitDir(path):
    for root,dirs,files in os.walk(path):
        for filepath in files:
            print os.path.join(root,filepath)

if __name__ == "__main__":
    path = r"E:\python_project\trunk\filedealing"
    VisitDir(path)
