#!/bin/env python
#enconding=utf-8
import urllib
import urllib2
import string
import re
from bs4 import BeautifulSoup
def baidu_search(search_url,all_url,txt):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    st_req = urllib2.Request(search_url, headers = headers)
    myRes = urllib2.urlopen(st_req)
    soup=BeautifulSoup(myRes,"lxml")
    get_url=soup.find_all('a',{'class':"cse-search-result_content_item_top_a"})
    get_name=soup.find_all('div',{'class':"cse-search-result_content_item_mid"})
    get_page=soup.find_all('div',{'class':"cse-search-result_paging_num"})
    lst=[] 
    for a in range(len(get_page)):
        page=int(get_page[a]['tabindex'])
        lst.append(page)
    lenth=len(lst)/2
    for b in range(lenth):
        end_url=all_url+str(b)+'0'
        print '*'*20+'Down loading the '+str(b)+' page'+'*'*20
        st_req = urllib2.Request(all_url, headers = headers)
        myRes = urllib2.urlopen(st_req)
        soup=BeautifulSoup(myRes,"lxml")
        getstart_url=soup.find_all('a',{'class':"cse-search-result_content_item_top_a"})
        getstart_name=soup.find_all('div',{'class':"cse-search-result_content_item_mid"})
        for i in range(len(getstart_url)):
            href=getstart_url[i]['href']
            for j in getstart_name[i].children:
                title=j.string.strip().encode('utf-8')
                f=open(txt,'a')
                f.writelines(href+'\n')
                f.writelines(title+'\n')
                f.close()
 
url=raw_input("please input the key world whitch you want to search :\n")
txt=str(raw_input("please input the filename to save your search for example:a.txt \n"))
search_url="http://www.wangpansou.cn/s.php?q="+url
all_url=search_url+'&wp=0&start='
baidu_search(search_url,all_url,txt) 



