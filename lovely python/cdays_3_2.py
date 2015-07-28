# -*- coding: utf-8 -*-
#
##################################################################################
# 读取某一简单索引文件cdays-3-test.txt，其每行格式为文档序号 关键词，
# 现需根据这些信息转化为倒排索引，即统计关键词在哪些文档中，
# 格式如下：包含该关键词的文档数 关键词 => 文档序号。
# 其中，原索引文件作为命令行参数传入主程序，
# 并设计一个collect函式统计 "关键字<－>序号" 结果对，最后在主程序中输出结果至屏幕。 
##################################################################################
#
import sys

def collect(file):
    '''改变key-value结构为value-key对
    @param file:文件对象
    @return: 一个dict包含value-key对
    '''
    result = {}
    for line in file.readlines():
        left,right = line.split()   # 以空格为分隔
        if result.has_key(right):   # 判断是否已经含有right值对应的key
            result[right].append(left)
        else:
            result[right] = [left]
    return result

if __name__ == "__main__":
    result = collect(open("cdays_3_2.txt","r"))
    for(right,lefts) in result.items():
        print "%d '%s'\t=>\t%s" % (len(lefts), right, lefts)
    
##print collect(open("cdays_3_2.txt","r"))
