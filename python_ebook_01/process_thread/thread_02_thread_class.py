#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading,time,random

### 使用threading的多线程程序框架
##class ThreadSkeleton(threading.Thread):
##
##    def __init__(self):   # 线程构造函数
##        threading.Thread.__init__(self)
##
##    def run(self):
##        pass
##
##thread = ThreadSkeleton()
##thread.start()

# 

##class ThreadDemo(threading.Thread):
##    def __init__(self,index,create_time):  # 线程构造函数
##        threading.Thread.__init__(self)
##        self.index = index
##        self.create_time = create_time

##    def run(self):     # 具体的线程运行代码
##        time.sleep(1)  # 休眠1秒钟
##        print ((time.time()-self.create_time),'-->',self.index)
##        print "Thread %d exit..."% (self.index)

##threads=[]
##
##for index in range(5):
##    thread = ThreadDemo(index,time.time())
##    thread.start()  # 启动线程
##    threads.append(thread)
##
##for thread in threads:
##    thread.join()   # 等待线程完成
##
##print "Main thread exit..."


# 线程中的局部变量，每个线程使用自己的私有变量thread.local方法

class ThreadDemo(threading.Thread):
    def __init__(self):   
        self.local = threading.local()   # 生成local数据对象

    def run(self):
        time.sleep(random.random())   # 随机休眠时间
        self.local.number = []
        for i in range(10):
            self.local.number.append(random.choice(range(10)))
        print threading.currentThread(),self.local.number

threadLocal = ThreadDemo()
threads=[]

for i in range(5):
    t = threading.Thread(target=threadLocal.run)
    t.start()  # 启动线程
    threads.append(t)

for i in range(5):
    threads[i].join()   # 等待线程完成

        
