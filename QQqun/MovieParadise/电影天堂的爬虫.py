#!/bin/env python
#encoding:utf-8
import urllib
import urllib2
import string
import re

def get(url,txt):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        st_req = urllib2.Request(url, headers = headers)
        myResponse = urllib2.urlopen(st_req)
        myPage = myResponse.read()
        unPage = myPage.decode("gbk",'ignore')
        enPage=unPage.encode("utf-8")
        myItems = re.findall('href="/html/gndy/.*?"',enPage)
        LST=[]
        for i in range(0,4):
            LST.append(myItems[i])
        for item in LST:
            item=item.replace('href="','').replace('"','')
            fsturl='http://www.ygdy8.net'+item
            ent_req = urllib2.Request(fsturl, headers = headers)
            enditems = re.findall("href='/html.*?'>2.*?<",enPage)
            for be_url in enditems:
                af_url=be_url.replace("href='","").replace("'>"," ")
                ed_url=af_url.split(' ')
                St_url=ed_url[0]
                ed_req=urllib2.Request(url+St_url,headers=headers)
                MyResponse=urllib2.urlopen(ed_req)
                MyPage=MyResponse.read()
                UnPage=MyPage.decode("gbk",'ignore')
		EnPage=UnPage.encode("utf-8")
		MyItems=re.findall('href="ftp.*?"',EnPage)
		lst=MyItems[0].replace('href="','').replace('"','')
		print lst
		f=open(txt,'a')
		f.writelines(lst+'\n')
		f.close

#st_url=str(raw_input("输入URL:\n"))
txt=str(raw_input("输入要保存的文件名:\n"))
st_url='http://www.ygdy8.net'
get(st_url,txt)


