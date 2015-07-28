# coding:utf-8
# 函数的返回值
from __future__ import division
def arithmetic(x,y,operator):
    result = {
        '+':x + y,
        '-':x - y,
        '*':x * y,
        '/':x / y
    }
    return result.get(operator)

print arithmetic(1,3,'+')

def func1():
    pass
print func1()

def func2():
    return
print func2()

def func3(x,y,z):
    l = [x,y,z]
    l.reverse()
    numbers = tuple(l)
    return numbers

x,y,z = func3(0,1,2)
print x,y,z

# 优化程序结构，return语句少用
def func4(x):
    if x > 0:
        result = 'x > 0'
    elif x == 0:
        result = 'x == 0'
    else:
        result = 'x < 0'
    return result
print func4(-2)

# 嵌套函数  外边定义
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def func5():
    x = 1
    y = 2
    m = 3
    n = 4
    return sum(x,y)*sub(m,n)

print func5()

# 嵌套函数  内部定义
def func6():
    x = 1
    y = 2
    m = 3
    n = 4
    def sum(a,b):
        return a + b
    def sub(m,n):
        return m - n
    return sum(x,y)*sub(m,n)
print func6()

# 函数递归
def refunc(n):
    i = 1
    if n > 1:
        i = n
        n = n * refunc(n -1)
    print '%d! ='%i,n
    return n

refunc(5)

# lambda函数
def func7():
    x = 1
    y = 2
    m = 3
    n = 4
    sum= lambda x,y:x + y
    print sum
    sub = lambda m,n:m - n
    print sub
    return sum(x,y)*sub(m,n)

print func7()

# 定义Generator函数
def func8(n):
    for i in range(n):
        yield i
# 在for循环中输出
for i in func8(3):
    print i
# 使用next()输出
r = func8(3)
print r.next()
print r.next()
print r.next()
# print r.next()  # 已经没有数据可生成，会产生异常

# yield 和 return语句的区别
def func9(n):
    for i in range(n):
        return i

def func10(n):
    for i in range(n):
        yield i

print func9(3)
f = func10(3)
print f
print f.next()
print f.next()
