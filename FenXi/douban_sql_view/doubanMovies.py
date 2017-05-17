# -*- coding: utf-8 -*-
# !/usr/bin/env python

from lxml import etree
import requests
import urllib2
import pymysql
import pymysql.cursors
import matplotlib.pyplot as plt
from pylab import *
import numpy as np

#必须设置默认编码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 连接mysql数据库
conn = pymysql.connect(host = '127.0.0.1',user = 'root', passwd = 'zjz4818774', db = 'douban', charset = 'utf8')
cur = conn.cursor()
cur.execute('use douban')

def get_page(i):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
    html = requests.get(url).content.decode('utf-8')
    # 读取页面的原始信息并将其从gbk转码
    #html = urllib2.urlopen(url).read().decode("utf-8")
    print "111111111111111111111111111111111111111"
    selector = etree.HTML(html)
    print selector
    print "111111111111111111111111111111111111111"
    content = selector.xpath('//div[@class="info"]/div[@class="bd"]/p/text()')
    print content

    for i in content[1::2]:
        print(str(i).strip().replace('\n\r', ''))
        # print(str(i).split('/'))
        i = str(i).split('/')
        i = i[len(i) - 1]
        # print('zhe' +ｉ)
        # print(i.strip())
        # print(i.strip().split(' '))
        key = i.strip().replace('\n', '').split(' ')
        print(key)
        for i in key:
            if i not in douban.keys():
                douban[i] = 1
            else:
                douban[i] += 1

def save_mysql():
    print douban
    for key in douban:
        print key
        print douban[key]
        if key != '':
            try:
                sql = 'insert douban(类别, 数量) value(' + "\'" + key + "\'," + "\'" + str(douban[key]) + "\'" + ');'
                cur.execute(sql)
                conn.commit()
            except:
                print '插入失败'
                conn.rollback()


def pylot_show():
        sql = 'select * from douban;'
        cur.execute(sql)
        rows = cur.fetchall()   # 把表中所有字段读取出来
        count = []   # 每个分类的数量
        category = []  # 分类

        for row in rows:
            count.append(int(row[2]))
            category.append(row[1])

        y_pos = np.arange(len(category))    # 定义y轴坐标数
        plt.barh(y_pos, count, align='center', alpha=0.4)  # alpha图表的填充不透明度(0~1)之间
        plt.yticks(y_pos, category)  # 在y轴上做分类名的标记

        for count, y_pos in zip(count, y_pos):
            # 分类个数在图中显示的位置，就是那些数字在柱状图尾部显示的数字
            plt.text(count, y_pos, count,  horizontalalignment='center', verticalalignment='center', weight='bold')
        plt.ylim(+28.0, -1.0) # 可视化范围，相当于规定y轴范围
        plt.title(u'豆瓣电影250')   # 图表的标题
        plt.ylabel(u'电影分类')     # 图表y轴的标记
        plt.subplots_adjust(bottom = 0.15)
        plt.xlabel(u'分类出现次数')  # 图表x轴的标记
        plt.savefig('douban.png')   # 保存图片

if __name__ == '__main__':
    douban = {}
    for i in range(0, 250, 25):
        get_page(i)
    save_mysql()
    pylot_show()
    cur.close()
    conn.close()