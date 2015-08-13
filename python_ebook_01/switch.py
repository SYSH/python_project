# coding:utf-8
# 创建一个switch类
class switch(object):
    def __init__(self,value):   # 初始化需要匹配的值value
        self.value = value
        self.fall = False    # 如果匹配到的case语句中没有break,则fall为true
    def __iter__(self):
        yield self.match     # 调用match方法返回一个生成器
        raise StopIteration    # StopIteration异常来判断for循环是否结束
    def match(self,* args):    # 模拟case子句的方法
        if self.fall or not args:    # 如果fall为true，则继续执行下面的case字句
                                # 或case子句没有匹配项，则流转到默认分支
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False
operator = "+"
x = 1
y = 2
for case in switch(operator):
    if case('+'):
        print x + y
        break
    if case('-'):
        print x - y
        break
    if case('*'):
        print x * y
        break
    if case('/'):
        print x / y
        break
    if case():      # 默认分支
        print ""


# 使用字典
from __future__ import division     
x = 1
y = 2
operator = "+"
result = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y

}
print result.get(operator)
