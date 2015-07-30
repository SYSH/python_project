#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import MySQLdb     # MySQLdb模块操作MySQL数据库很方便,使用前需先安装


try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='lovemysql',db='mysql_shiyan')
except Exception,e:
    print e
    print "连接数据库失败"
    sys.exit()

try:
        
    # 获取cursor(游标)
    cursor = conn.cursor()

    # 增
    try:       
        sql = "INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(%s,%s,%s,%s,%s,%s)"
        value = ('13','Job','42','4000','123321','dpt4')
        cursor.execute(sql,value)
        conn.commit()
    except Exception,e:
        conn.rollback()
        print e
        print "INSERT新增数据出现错误"
            

    # 删
    try:
        sql = "DELETE FROM employee WHERE id=13"
        cursor.execute(sql)
        conn.commit()
    except Exception,e:
        conn.rollback()
        print e
        print "DELETE出现错误"

    # 改
    try:
        sql = "UPDATE employee SET name = %s,salary = %s WHERE id = %s"
        value = ('Jobs','3700','13')
        cursor.execute(sql,value)
        conn.commit()
    except Exception,e:
        conn.rollback()
        print e
        print "UPDATE出现错误"

    # 查
    try:
        sql = "SELECT * FROM employee"
        print sql
        cursor.execute(sql)
        data = cursor.fetchall()
        for index in range(len(data)):
            print data[index]
    except Exception,e:
        print e
        print "SELECT查找数据出现错误"
    
except Exception:
    print "处理时出现异常"
finally:
    cursor.close()  # 关闭游标
    conn.close()    # 关闭数据库
