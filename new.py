# coding:utf-8
list = ['apple','banana','orange','grape']
print list
print list[2]
list.append('watermelon')
list.insert(1,'grapefruit')
print list
list.remove('grape')
print list
print list.pop()
print list

print list[-2]
print list[1:3]
print list[-3:-1]
list = [['apple','banana'],['grape','orange'],['watermelon'],['gragefruit']]
for i in range(len(list)):
    print "list[%d]:"% i,"",
    for j in range(len(list[i])):
        print list[i][j],"",
    print

list1 = ['apple','banana']
list2 = ['grape','orange']
list1.extend(list2)
print list1
list3 = ['watermelon']
list1 = list1 + list3
print list1
list1 += ['grapefruit']
print list1
list1 = ['apple','orange'] * 2
print list1
list = ['apple','orange','grape','watermelon','banana']
print list.index('grape')
print list.index('orange')
print 'orange' in list
list.sort()
print "Sorted list:",list
list.reverse()
print "Reversed list:",list
# 堆栈
list.append("peach")
print list
print "弹出的元素:",list.pop()
print list
# 队列
list.append("peach")
print list
print "弹出的元素:",list.pop(0)
print list
dict = {'a':'apple','b':'banana','g':'grape','o':"orange"}
print dict
print dict['a']

dict = {1:"apple",2:'orange',3:'banana',4:'grape'}
print dict
print dict[3]
print '------------------------------------------------------'
dict = {'a':'apple','b':'banana','g':'grape','o':'orange'}
dict['w'] = 'watermelon'
del(dict['a'])
dict['g']='grapefruit'
print dict.pop('b')
print dict
dict.clear()
print dict

# 字典的遍历
dict = {'a':'apple','b':'banana','g':'grape','o':'orange'}
for k in dict:
    print 'dict[%s]:'% k,dict[k]
print dict.items()
for (k,v) in dict.items():
    print 'dict[%s]='% k,v
print dict.iteritems()
for k,v in dict.iteritems():
    print 'dict[%s]='% k,v
for (k,v) in zip(dict.iterkeys(),dict.itervalues()):
    print 'dict[%s]='% k,v

# 混合字典
print '----------------------------------------------------'
dict = {'a':('apple',),'bo':{'b':'banana','o':'orange'},'g':['grape','grapefruit']}
print dict['a']
print dict['a'][0]
print dict['bo']
print dict['bo']['o']
print dict['g']
print dict['g'][1]


# 字典的方法
dict = {'a':'apple','b':'banana','c':'grape','d':'orange'}
# 输出key的列表
print dict.keys()
# 输出value的列表
print dict.values()

# get()方法
print dict.get('c','apple')
print dict.get('e','apple')
print dict.get('m','None')

# update()方法
dict1 = {'a':'apple','b':'banana'}
dict2 = {'c':'grape','d':'orange'}
dict1.update(dict2)
print dict1

# setdefault()方法：设置默认值
dict = {}
dict.setdefault('a')
print dict
dict['a'] = 'apple'
dict.setdefault('a','default')
print dict

# 调用sorted()实现字典的排序
dict = {'a':'apple','b':'banana','c':'orange','d':'grape'}
print dict
# 按照key排序
print sorted(dict.items(),key = lambda d:d[0])
# 按照value排序
print sorted(dict.items(),key = lambda d:d[1])
print '------------------------------------------------'

# 字典的浅拷贝:浅拷贝只是复制数据，数据的引用没有被复制，因此新的数据和旧的数据使用同一块内存空间
dict1 = {'a':'apple','b':'grape'}
dict2 = {'c':'orange','d':'banana'}
dict2 = dict1.copy()
print dict2

# 字典的深拷贝
import copy
dict = {'a':'apple','b':{'g':'grape','o':'orange'}}
dict2 = copy.deepcopy(dict)
dict3 = copy.copy(dict)
dict2['b']['g'] = 'orange'   # 深拷贝 其改变不影响原来的数据
print dict
dict3['b']['g'] = 'orange'   # 浅拷贝 会改变数据
print dict

# 全局字典 sys.modules
import sys
print sys.modules.keys()
print sys.modules.values()
print sys.modules['os']

# import sys
d = sys.modules.copy()
import copy,string
print zip(set(sys.modules) - set(d))
