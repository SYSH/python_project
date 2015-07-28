# -*- coding: UTF-8 -*-
#
# 判断是否为闰年
import time

def isLeapYear(n):
    if (n%4000 == 0) or (n % 4 == 0 and n % 100 != 0):
        result = "% d is a leap year!"%n
    else:
        result = "% d isn't a leap year!"%n
    print result


thisyear = time.localtime()[0]    # 获取今年的年份
isLeapYear(thisyear)
