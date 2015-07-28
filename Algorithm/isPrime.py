# -*- coding: UTF-8 -*-
#
# 判断 N 之内的素数有哪些并计数
import math

def isPrime(n):
    count = 0;   # 素数的数目
    if n <= 1:
        print "Wrong number!"
    else:
        for i in range(2,n+1):
            for j in range(2,int((i ** 0.5)+1)):   # or   math.sqrt(i)
                if( i % j == 0 ):
                    break;
            else:
                count += 1
                print i,
    print "\nPrime count = %d"%count

isPrime(1000)
