#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# 使用urlparse解析URL
#
import urlparse

# 解析URL-->urlparse
r = urlparse.urlparse("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=python%202.7%20urlparse%202015&rsv_spt=1&oq=python%202.7%20urlparse&rsv_pq=c14fb10d00007826&rsv_t=d32daD5FvKfEMIU2qndX%2BnOyXd%2FS8TLoWe7gvH3Iw1NQJb5widQHVhPAjcki3sYYYap8&rsv_enter=0&inputT=2579&rsv_sug3=70&rsv_sug1=38&rsv_sug2=0&rsv_sug4=2979&rsv_sug=1")
print r
print r.scheme     # 协议
print r.netloc     # 服务器地址
print r.path       # 路径
print r.params     # 参数
print r.query      # 查询部分
print r.fragment   # 分片部分
print r.username   # 用户名
print r.password   # 密码
print r.hostname   # 主机名
print r.port       # 端口号
print r.geturl()   # 通过URL六元组得到URL信息

# URL合并-->urljoin("绝对地址","相对地址")
r = urlparse.urljoin("https://www.baidu.com/","guol/blog/95699")
print r
# 两个参数为空，则URL为一个空字符串
r = urlparse.urljoin("","")   
print r
# 若相对地址中有协议字段，优先使用相对URL中的协议
r = urlparse.urljoin("ftp://www.baidu.com/","https://www.baidu.com/news")
print r
# 当相对地址不包含协议的时候，就会将所有字符串认为是一个路径信息，从而和绝对地址URL结合起来
r = urlparse.urljoin("https://www.baidu.com/","www.baidu.com/news")
print r
# 需要拼合的两个URL中的服务器地址不同的，拼合采用相对URL中的服务器地址
r = urlparse.urljoin("https://www.baidu.org","https://www.baidu.com/news")
print r

# URL分解-->urlsplit("URL")-->反方法：urlunsplit(五元组)
r = urlparse.urlsplit("http://baike.baidu.com/link?url=eWzaRtpmLkvIgrTRvMwHYVZClEUlTZrMQIpJABi9kdtxL_Dh6u6nzflrEFeEKF6KgvxUPkuk16p2ORkUnuK7QbdS9GyYSVZcXJe8yOmDvBa")
print r
# urlsplit()和urlunsplit()组合在一起使得可以有效的格式化URL,特殊字符在这个过程中可以得到转化
r = urlparse.urlunsplit(urlparse.urlsplit("http://baike.baidu.com/link?"))
print r


# urljoin/urlsplit/urlunsplit这3个方法的区别

abs_urls = ["http://www.python.org","ftp://www.linux.org","http://www.gtk.org","file://"]
rel_url = "faq.html"

for abs_url in abs_urls:
    url = urlparse.urljoin(abs_url,rel_url)   # 拼合URL
    expected_url = url
    scheme,netloc,path,query,fragment = urlparse.urlsplit(url) # 分解URL

    if scheme and scheme=="file":
        print url,"==>None"
        continue
    if scheme is "ftp":
        expected_url = urlunsplit(("http",netloc,path,query,fragment))  # 合并URL                              
    print url,"==>",expected_url
