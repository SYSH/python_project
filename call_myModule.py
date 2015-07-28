# coding:utf-8
# 调用自定义模块的类和函数
import myModule

print "count = ",myModule.func()
myModule.count = 10
print "count = ",myModule.count

import myModule
print "count = ",myModule.func()


if myModule.count > 1:
    myModule.count = 1
else:
    import myModule
print "count = ",myModule.count


import myModule
print __doc__
