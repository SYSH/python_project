#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Exception example 01-->try...except...的用法

try:
    file("hello.txt",'r')
    print "读文件"
except IOError:
    print "文件不存在"
except:
    print "程序异常"

print '--------------------------------------'

# Exception example 02

try:
    result = 10/0
except ZeroDivisionError:
    print "0不能做除数"
else:
    print result

print '--------------------------------------'

# Exception example 03

try:
    s = 'hello'
    try:
        print s[0] + s[1]
        print s[0] - s[1]
    except TypeError:
        print "字符串不支持减法运算"
except:
    print '异常'

print '--------------------------------------'

# Exception example 04-->try...finally...的用法

# finally错误的用法

try:
    f=open('hello.txt','r')
    try:
        print f.read(5)
    except:
        print "读取文件错误"
    finally:
        print "释放资源"
        f.close()
except IOError:
    print '文件不存在'

print '--------------------------------------'

# Exception example 05-->使用raise抛出异常

try:
    s = None
    if s is None:
        print "s是空对象"
        raise NameError
    print len(s)
except TypeError:
    print "空对象没有长度"




