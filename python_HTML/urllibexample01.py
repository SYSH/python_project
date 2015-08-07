#! /usr/bin/env python
# coding: utf-8

# urllib中对URL进行编码和解码
# quote:对URL进行编码   quote_plus:同quote方法，进一步将空格表示成"+"符号
# unquote:对URL进行解码   unquote_plus:同unquote方法,进一步将空格转化为"+"号

import urllib

# 编码和解码是互逆的
r1 = urllib.quote("/~test/")
print r1
r2 = urllib.quote("/~test/public html")
print r2
r3 = urllib.quote_plus(" /~test/public html")
print r3

print urllib.unquote_plus(r3)
print urllib.unquote(r2)
r = urllib.quote(" /~test/"," ~/")
print r

# 中文编解码

r = urllib.quote("URL编码")
print  r
print urllib.unquote(r)


# 查询参数的编码urllib->urlencode:将查询的参数对返回为URL编码形式
r = urllib.urlencode([('keyword1','value1'),('keyword2','value2')])
print r
a = urllib.urlencode({'keyword1':'value1','keyword2':'value2'})
print a
b = urllib.urlencode({'keyword2':'value2','keyword1':'value1'})
print b
print a is b
print a==b

# urlencode可以接受一个可选参数，用来对输入查询参数中的数据进行控制,默认是False
# 即当(keyword,value)中value也为一个列表时，默认False下，将其整个使用作为查询参数
# 若为True时，将value列表中的每个值都和keyword组成一个查询参数对

r1 = urllib.urlencode([('keyword',('value1','value2','value3'))])
print r1
r2 = urllib.urlencode([('keyword',('value1','value2','value3'))],True)
print r2

