#! usr/bin/env python
# -*- coding: utf-8 -*-

# 如果类中某属性定义为一个数列，则使用__getitem__()输出系列中的各个元素

class FruitShop:
    def __getitem__(self,i):
        return self.fruits[i]

if __name__ == "__main__":
    shop = FruitShop()
    shop.fruits = ['apple','banana']
    print shop[1]
    for item in shop:   # 输出水果店的水果
        print item
            
print '------------------------------------------'

# __str__()用于表示对象代表的含义，返回一个字符串,此函数必须使用return 返回，否则会出错

class Fruit:
    '''Fruit类'''
    def __str__(self):       # 定义对象的字符串表示
        return self.__doc__

    
if __name__ == "__main__":
    fruit = Fruit()
    print str(fruit)         # 调用__str__
    print fruit

print '------------------------------------------'

# __call__()可以在对象创建时直接返回__call__()的内容。使用该方法可以模拟静态方法

class Fruit:
    class Growth:     # 内部类
        def __call__(self):
            print "grow..."

    grow = Growth()   # 返回call的内部   类Growth作为函数返回，即为外部类Fruit定义方法grow()

if __name__ == "__main__":
    fruit = Fruit()
    fruit.grow()
    fruit.grow()

