# coding:utf-8
# 自定义模块
count = 1

def func():
    global count
    count = count + 1
    return count


if __name__ == '__main__':
    print 'myModule作为主程序运行'
else:
    print 'myModule被另一个模块调用'
