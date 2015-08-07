#! /usr/bin/env python
# encoding: utf-8

import urllib

def reporthook(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent

def download(url,filename=""):
    def report(block_count,block_size,file_size):
        if file_size == -1:
            print "Can't determine the file size,now retrieved",block_count*block_size
        else:
            percentage = int((block_count* block_size*100.0)/file_size)
            if percentage > 100:
                print " 100%"
            else:
                print "% d% %"%(percentage)

    filehandler,m = urllib.urlretrieve(url,filename,reporthook=reporthook)
    print "Done"
    return filehandler



download("http://www.sina.com.cn","E:\\sina.html")
