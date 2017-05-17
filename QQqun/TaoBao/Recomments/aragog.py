# -*- coding: utf-8 -*-
# __author__ = 'seven'

#淘宝爬虫
import os, urllib2, datetime
from sys import argv
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup

timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
path = os.getcwd()
keywords = []
keyword = ''

    #接收存储路径和关键字
if len(argv) > 2:
        path = argv[1]
        keywords = argv[2:]

def aragog(url, analyze_func):
        '''
        爬虫入口
        '''
        print url
        page = urllib2.urlopen(url, timeout=20)
        if page.code != 200:
            insert_log('request,{0},{1}'.format(page.code, url))
            return
        try:
            page = page.read().decode('gbk').encode('utf-8')
        except Exception:
            insert_log('unicode,转码错误,' + url)
            return
        else:
            soup = BeautifulSoup(page)
            #给BeautifulSoup添加url属性，存放当前页面的URL
            soup.url = url
            return analyze_func(soup)

def insert_log(record):
        '''
        打印错误日志
        '''
        with open(path + '/log.csv', 'a') as log:
            log.write('{time},{record},\r\n'.format(
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                record = record
            ))

def get_pages_total(soup):
        '''
        获得搜索结果的页数
        '''
        try:
            return int(soup.find('span', {'class' : 'page-info'}).string.split('/')[1])
        except Exception:
            insert_log('analyze,获取页数失败,' + soup.url)
            return 0

def analyze_search(soup):
        '''
        搜索结果页面解析
        '''
        for item in soup.find('div', {'id' : 'list-content'}).findAll('li', {'class' : 'list-item'}):
            try:
                record = to_utf8(format_item_url(item.h3.a['href'])) + ','
                record += to_utf8(item.h3.a['title']) + ','
                record += to_utf8(item.find('li', {'class' : 'price'}).em.string) + ','
                record += to_utf8(item.find('li', {'class' : 'seller'}).a.string) + ','
                record += to_utf8(item.find('span', {'class' : 'loc'}).string) + ','
            except Exception:
                insert_log('analyze,页面解析错误,' + soup.url)
            else:
                with open('{path}/{time}_{keyword}.csv'.format(
                    path = path,
                    time = timestamp,
                    keyword = keyword
                ), 'a') as data:
                    data.write(record + '\r\n')

def analyze_item(soup):
        if 'chaoshi' in soup.url:
            return analyze_item_chaoshi(soup)
        elif 'tmall' in soup.url:
            return analyze_item_tmall(soup)
        else:
            return analyze_item_taobao(soup)

def analyze_item_tmall(soup):
        '''
        天猫页面解析
        '''
        try:
            record = to_utf8(urlparse(soup.find('div', {'class' : 'shop-intro'})\
                .find('a', {'class' : 'enter'})['href']).hostname) + ','
            record += to_utf8(soup.find('li', {'class' : 'tb-clearfix'}).text) + ','
            record += to_utf8(soup.find('em', {'class' : 'J_MonSalesNum'}).string) + ','
        except Exception:
            insert_log('analyze,页面解析错误,' + soup.url)
            return ''
        else:
            return record

def analyze_item_taobao(soup):
        '''
        淘宝页面解析
        '''
        if len(soup.text) > 200:
            try:
                record = to_utf8(urlparse(soup.find('a', {'class' : 'tb-enter-shop'})[
                               'href']).hostname) + ','
                record += to_utf8(soup.find('li', {'class' : 'tb-clearfix'}).text) + ','
                record += to_utf8(soup.find('em', {'class' : 'J_TDealCount'})
                    .string) + ','
            except Exception:
                insert_log('analyze,页面解析错误,' + soup.url)
                return ''
            else:
                return record
        else:
            return aragog(soup.url.replace('://item', '://meal'), analyze_item_taobao)


def analyze_item_chaoshi(soup):
        '''
        天猫超市页面解析
        '''
        try:
            record = 'http://chaoshi.tmall.com,'
            record += to_utf8(soup.find('ul', {'class' : 'tb-meta'}).findAll(
                'li')[3].text) + ','
            record += to_utf8(soup.find('li', {'class' : 'tb-sold-out'}).em
                .string) + ','
        except Exception:
            insert_log('analyze,页面解析错误,' + soup.url)
            return ''
        else:
            return record

def query_2_dict(query):
        '''
        将URL的query由字符串转为字典
        '''
        return eval('{\''+query.replace('=', '\':\'').replace('&', '\',\'')+'\'}')

def format_item_url(url):
        '''
        去掉产品页面URL中query中无关的数据
        淘宝产品页面有五种『淘宝，天猫，推广产品，天猫超市，淘宝生态农业』
        其中淘宝生态农业页面有淘宝产品页面通过js指向过去，这里暂不考虑
        淘宝和天猫规则一样
        推广产品里面url包含‘ju.juatpanel.com，去掉即可
        天猫超市直接返回
        '''
        if 'ju.atpanel.com' in url:
            url = urlparse(url).query[4:]
            url = format_item_url(url)
        elif not 'chaoshi' in url:
            try:
                parse = urlparse(url)
                url = "http://{0}{1}?id={2}".format(parse.netloc,
                    parse.path, query_2_dict(parse.query)['id'])
            except Exception:
                insert_log('url,'+url)
        return url


def to_utf8(string):
        '''
        字符由unicode转为utf-8
        '''
        if isinstance(string, unicode):
            string = string.encode('utf-8')
        if string == None:
            string = ''
        return string

if __name__ == '__main__':
        #获取产品列表
        for keyword in keywords:
            keyword = keyword
            search_url = 'http://s.taobao.com/search?q=' + urllib2.quote(keyword)
            for i in range(aragog(search_url, get_pages_total)):
                aragog('{0}&s={1}'.format(search_url, i*40), analyze_search)
        #获取产品详情
        for keyword in ['核桃']:
            lines = []
            with open('{path}/{time}_{keyword}.csv'.format(
                path = path,
                time = timestamp,
                keyword = keyword
            ), 'r') as data:
                for line in data.readlines():
                    new_line = aragog(line.split(',')[0], analyze_item)
                    lines.append(line.replace('\n', ',' + new_line + '\r\n'))
            with open('{path}/{time}_{keyword}.csv'.format(
                path = path,
                time = timestamp,
                keyword = keyword
            ), 'w') as data:
                data.writelines(lines)

