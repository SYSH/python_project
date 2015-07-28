# coding:utf-8

# 内置函数apply()
def sum(x=1,y=2):
    return x + y

print apply(sum,(1,3))

# filter()函数
def func(x):
    if x > 0:
        return x
print filter(func,range(-9,10))

print '---------------------------------------'
# reduce()函数
def sum(x,y):
    return x + y

print reduce(sum,range(0,10))
print reduce(sum,range(0,10),10)
print reduce(sum,range(0,0),10)

print '---------------------------------------'
# map()函数
def power(x): return x ** x
print map(power,range(1,5))

def power2(x,y):return x ** y
print map(power2,range(1,5),range(5,1,-1))
