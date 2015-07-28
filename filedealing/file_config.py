# -*-coding:UTF-8 -*-
#
# 读配置文件
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("ODBC.ini")
sections = config.sections()
print "配置块:",sections
o = config.options("ODBC 64 bit Data Sources")
print "配置项:",o
v = config.items("ODBC 64 bit Data Sources")
print "内容:",v

# 根据配置块和配置项返回内容
access = config.get("ODBC 64 bit Data Sources","MS Access Database")
print access
excel = config.get("ODBC 64 bit Data Sources","Excel Files")
print excel
dBASE = config.get("ODBC 64 bit Data Sources","dBASE Files")
print DBASE
