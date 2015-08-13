# -*- coding: UTF-8 -*-
# 设计并调用函数showFileProperties(),列出"C:\Users\Rui\Desktop\filedealing"路径下的所有文件
def showFileProperties(path):
    # "显示文件属性。包括路径、大小、创建日期、最后修改时间，最后到访时间"
    import time,os
    for root,dirs,files in os.walk(path,True):
        print "位置:" + root
        for filename in files:
            state = os.stat(os.path.join(root,filename))
            info = "文件名:" + filename + ""
            info = info + "大小:" + ("%d"% state[-4]) + ""
            t = time.strftime("%Y-%m-%d %X",time.localtime(state[-1]))
            info = info + "创建时间:" + t + ""
            t = time.strftime("%Y-%m-%d %X",time.localtime(state[-2]))
            info = info + "最后的修改时间:" + t + ""
            t = time.strftime("%Y-%m-%d %X",time.localtime(state[-3]))
            info = info + "最后的访问时间:" + t + ""
            print info

if __name__ == "__main__":
    path = r"C:\Users\Rui\Desktop\filedealing"
    showFileProperties(path)
