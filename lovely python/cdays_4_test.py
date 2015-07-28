# -*- coding: utf-8 -*-
#
# 读取文件cdays−4-test.txt 内容，去除空行和注释行后，
# 以行为单位进行排序，并将结果输出为cdays−4-result.txt。
#

f = file("cdays_4_test.txt",'r')
newf = file("cdays_4_result.txt","w")
lines = f.readlines()
export = []
for line in lines:
    if line.startswith("#") or not line.split():     ## line[0] == "#" or not len(line)
        continue
    else:
        newf.writelines(line)
f.close()
newf.close()
