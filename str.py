# -*-coding:utf-8-*-
# 格式化字符串
str1 = 'version'
num = 1.0
forma = '%s'% str1
print forma
forma = '%s %d'%(str1,num)
print forma

# 带精度的格式化
print "浮点型数字:% f"% 1.25
print "浮点型数字:% .1f" % 1.25
print "浮点型数字:% .2f" % 1.254

# 使用字典格式化字符串
print '%(version)s:%(num).1f'%{'version':'version','num':2}

# 字符串对齐
word = 'version3.0'
print word.center(20)
print word.center(20,'*')
print word.ljust(0)
print word.rjust(20)
print '%30s'% word

# 输出转义字符
path = "hello\tworld\n"
print path
print len(path)
path = r"Hello\tWorld\n"
print path
print len(path)

# 去掉转义字符
word = "\tHello world\n"
print '直接输出:',word
print 'strip()后输出',word.strip()
print 'lstrip()后输出',word.lstrip()
print 'rstrip()后输出',word.rstrip()

# 字符串链接方法
str1 = 'hello '
str2 = 'world '
str3 = 'hello '
str4 = 'china '
result = str1 + str2 + str3
result += str4
print result

# 使用join()连接字符串
str0 = ['hello ','world ','hello ','china ']
result = "".join(str0)
print result

# 字符串的截取
word = "world"
print word[3]
str5 = "hello world"
print word[0:3]
print str5[::2]
print str5[1::2]

# 使用split()函数实现截取多个子串
sentence = "Bob said:1,2,3,4"
print "使用空格截取子串:",sentence.split()
print "使用逗号截取子串:",sentence.split(",")
print "使用两个逗号取子串:",sentence.split(",",2)

# 字符串连接后，Python将分配新的内部空间给连接后的字符串
strr = 'a'
print id(strr)
print id(strr + 'b')

# 字符串的比较
str1 = 1
str2 = '1'
if str1 == str2:
    print '相同'
else:
    print '不相同'
if str(str1) == str2:
    print 'same'
else:
    print '不相同'

#比较字符串的开始和结束
word = 'Hello World'
print 'Hello' == word[0:5]
print word.startswith('Hello')
print word.endswith('ld',6)
print word.endswith('ld',6,10)
print word.endswith('ld',6,len(word))

# 字符串的反转 Python没有提供字符串反转的函数，可以用列表和字符串来实现字符串反转，并通过range()进行循环
# 循环输出反转
def reverse(s):
    out = ""
    li = list(s)
    for i in range(len(li),0,-1):
        out += "".join(li[i-1])
    return out

print reverse('hello')

# 使用list的reverse
def reverse(s):
    li = list(s)
    li.reverse()
    s = "".join(li)
    return s

print reverse('world')

# 字符串的查找和替换
# 查找字符串
sentence = "This is a apple."
print sentence.find('a')
sentence = "This is a apple."
print sentence.rfind("a")

# 字符串的替换
centence = "hello world,hello china"
print centence.replace("hello","hi")
print centence.replace("hello","hi",1)
print centence.replace("abc",'hi')

# 字符串与日期的转换
# 时间到字符串的转换:strftime()
# 字符串到时间的转换:strptime()->datetime()函数
import time,datetime

# 时间到字符串的转换
print time.strftime("%Y-%m-%d %X",time.localtime())
# 字符串到时间的转换
t = time.strptime("2008-08-08","%Y-%m-%d")
y,m,d = t[0:3]
print datetime.datetime(y,m,d)



