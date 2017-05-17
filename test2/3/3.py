# coding=utf-8
import urllib2
try:
    response = urllib2.urlopen('http://bbs.csdn.net/why')
except urllib2.HTTPError, e:
    print e.code
print
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

print
print
# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.1
#   作者：why
#   日期：2013-05-14
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#---------------------------------------

import string, urllib2

def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,5) + '.html'
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
        f = open(sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()


#-------- 在这里输入参数 ------------------

# 这个是百度贴吧中某一个帖子的地址

#iPostBegin = 1
#iPostEnd = 10
#这里是用来和用户交互的

#bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
bdurl = 'http://tieba.baidu.com/p/4773174704?pn='
begin_page = int(raw_input(u'请输入开始的页数：\n'))
end_page = int(raw_input(u'请输入终点的页数：\n'))
#-------- 在这里输入参数 ------------------


#调用
baidu_tieba(bdurl,begin_page,end_page)