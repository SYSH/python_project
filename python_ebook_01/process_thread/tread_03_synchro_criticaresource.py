#! /usr/bin/env python
# -*- coding: utf-8 -*-

# critical resource:临界资源和临界区：指一次只允许一个线程访问的资源，临界资源的共享只能使用互斥方式。

# 演示引入一个全局的计算器方法

import threading
import time

class Counter:  # 计算器类
    def __init__(self):
        self.value = 0
##        self.lock=thread.allocate_lock()   # 低层次的thread锁机制  生成互斥锁，初始化未锁
        self.lock=threading.Lock()         # 高层次的threading锁机制 生成互斥锁，初始化未锁
        
    def increment(self):
        self.lock.acquire()       # 获取锁,进入临界区-->加锁
        self.value=self.value+1   # 将value值加1
        value = self.value   # 并返回这个value值
        self.lock.release()       # 释放锁，离开临界区-->解锁
        return value

counter = Counter()

class ThreadDemo(threading.Thread):
    def __init__(self,index,create_time):
        threading.Thread.__init__(self)
        self.index = index
        self.create_time = create_time

    def run(self):
        time.sleep(1)
        value = counter.increment()
        print ((time.time()-self.create_time),self.index,value)

for index in range(100):
    thread = ThreadDemo(index,time.time())
    thread.start()
