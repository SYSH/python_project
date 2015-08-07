#! /usr/bin/env python
# coding:utf-8

import urllib2

fp = urllib2.urlopen("https://www.shiyanlou.com/")
print fp.read()
print fp.geturl()
print fp.info().items()
