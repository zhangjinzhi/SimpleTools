#coding=utf-8
import requests
import re
import Queue
import MySQLdb
import gevent
from gevent.threadpool import ThreadPool

#def conn_sql():
    #conn=MySQLdb.connect(
        #host='localhost',
        #port=3306,
        #user='root',
        #passwd='1234',
       # db='zhihu',
      #  charset='uft8'
     #   )
    #cur=conn.cursor()
   # return conn,cur

def get_ip(text):
    '''针对西刺代理网页编码建立的规则,此规则只爬取HTTPS类型的代理地址。返回的格式 （ip，端口）'''
    rex=r'''<td class="country"><img src=.*?/></td>\s*?<td>(.*?)</td>\s*?<td>(.*?)</td>\s*?<td>\s*.*\s*</td>\s*?.*\s*?<td>HTTPS</td>'''
    ip=re.findall(rex,text)
    return ip

url=[
    'http://www.xicidaili.com/nn/1',
    'http://www.xicidaili.com/nn/2',
    'http://www.xicidaili.com/nt/1',
    'http://www.xicidaili.com/nt/2',
    'http://www.xicidaili.com/wn/1',
    'http://www.xicidaili.com/wn/2',
    'http://www.xicidaili.com/wt/1',
    'http://www.xicidaili.com/wt/2',
    ]
##爬取西刺代理各分类前两页
def create_pool(url):
    '''创建代理池，说白了就是代理列表.起初是打算用队列的，后来考虑到要验证每个代理，取出还要再插回去麻烦'''
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWIxYjAwZDkxMDE1NWRiYjAwMTBjZTFjZGY3YjJjMjE4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXE5aGt6cDdPU2tyajI4RjB2dENmZS9aT0RMTDVTK1R2d1hTMDVjUGYxT0E9BjsARg%3D%3D--a913aa7825c13fec2fdfd583519c69b3345ab87b; CNZZDATA1256960793=284076470-1468134027-null%7C1468307148',
        'DNT':'1',
        'Host':'www.xicidaili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36'
        }
    ##自定义头，找个浏览器开发者模式复制一下
    data=[]
    #用来存储抓取的原始数据
    proxy_pool=[]
    #初始化代理列表
    #p={'http':'81.139.247.236:80'}
    ##p是一个http代理，有时爬多了西刺代理就禁止访问了
    ###用代理去爬代理挺那啥的。。所以后面实际使用中可视网站更新状况自定义轮询代理网站的时间
    for i in url:
        r=requests.get(i,headers=headers)#如果用代理把代理加进去
        text=r.text
        print r.status_code
        ip=get_ip(text)
        data.extend(ip)
        #用extend是为了格式上方便，方便遍历
    for i in data:
        ip=i[0]+':'+i[1]
        #组合ip+port
        proxy_pool.append(ip)
        #存在表里
    return proxy_pool

def test_proxy(ip,proxy_pool,headers):
    '''测试代理是否可用，免费的代理挺不稳定的。使用率较低'''
    try:
        r=requests.get('https://www.zhihu.com',proxies={'https':ip},headers=headers)
        status=r.status_code
        print
        if status==200:
            print ip,'200'
        #主要根据返回的状态码判断

    except:
        proxy_pool.remove(ip)
        #这一步是抛弃队列用列表列表的直接原因
        #就感觉很省事。另外也可以避免参数在多个函数间传递的问题
        pass
    return proxy_pool

headers={
    'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Language':'zh-CN',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host':'www.zhihu.com',
    'Connection':'Keep-Alive',
    'Cookie':'n_c=1; __utmc=51854390; q_c1=6879d12c58854a25a7baa63bd647c17f|1468227004000|1468227004000; l_cap_id="NmIzZDAxM2IyNDA4NDUxYmFiYzRhZjBhYjBiZGIxMGM=|1468227004|d39c2d05c63f5a30ac21b24beb6a48e0648c70bb"; cap_id="OWUyMGVhNTAxNjExNDQ5YWE2M2EyODkwYjdkOWNjOGQ=|1468227004|76ebb55701b78072ac6a2ee080d5f0c5dadc292b"; d_c0="AJBAWDZdNgqPTlKnUijCIex0WCt8K2FtfhM=|1468227005"; _zap=884bd241-ddd0-430a-b8ab-97a026efabd0; __utma=51854390.2013250603.1468227006.1468227006.1468227006.1; __utmb=51854390.11.9.1468227042707; __utmz=51854390.1468227006.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20160711=1; __utmt=1; _xsrf=179e610b488529dd83ffbfb4bc6a6beb; _za=fa119adb-56a9-4213-a9bc-438a300afd85',
    }
#定义一个访问知乎的头

def multi_thread_test(proxy_pool):
    '''上面那个测试可以直接用但时间太长了。所以用并发来解决。不过总体时间还是挺长的'''
    n=len(proxy_pool)
    pool=ThreadPool(n)
    #最大的线程数等于代理总数，这样就可以所有代理同时跑
    for ip in proxy_pool:
        pool.spawn(test_proxy,ip,proxy_pool,headers)
    gevent.wait()
    return proxy_pool

def test():
    '''测试结果'''
    from time import *
    t1=time()
    proxy_pool=create_pool(url)
    proxy_pool=multi_thread_test(proxy_pool)
    print proxy_pool
    t2=time()
    print t2-t1
test()

