# -*-coding:utf-8-*-

# 创建文件
context = "hello world\n\
hello China"

f = file('hello.txt','w')    # 打开文件
f.write(context)             # 把字符串写入文件
f.close()                    # 关闭文件

# 文件的读取
# 按行读取readline()
f = open("hello.txt")
while True:
    line = f.readline()
    if line:
        print line,
    else:
        break
f.close

print "\n"

# 多行读取readlines()
f = file("hello.txt")
lines = f.readlines()
for line in lines:
    print line,

print '\n'

# 一次性读取read()
f = open('hello.txt')
context = f.read()
print context

print '\n'

# 通过read()参数的值，返回指定字节
f = open('hello.txt')
context = f.read(5)
print context
print f.tell()
context = f.read(5)
print context
print f.tell()
f.close()

# 文件的写入
# 使用writelines()写入
f = file("hello.txt","w+")
li = ['Hello World\n','Hello China\n']
f.writelines(li)
f.close()

# 追加新的内容到文件
f = file('hello.txt','a+')
new_context = 'goodbye'
f.write(new_context)
f.close
