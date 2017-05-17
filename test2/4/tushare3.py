# -*- coding:utf-8 -*-
import tushare as ts

#print ts.get_h_data('600848')

#df = ts.realtime_boxoffice()
#print df

#df = ts.day_boxoffice() #取上一日的数据
#df = ts.day_boxoffice('2015-12-24')  #取指定日期的数据
#print df

#print ts.get_hist_data('600848', ktype='W') #获取周k线数据
#print ts.get_hist_data('600848')

#print ts.get_latest_news()#看最新的新闻

#print ts.get_cpi()#查看宏观经济指数，如：居民消费指数

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#print ts.get_stock_basics()

def get_all_price(code_list):
    '''''process all stock'''
    df = ts.get_realtime_quotes(STOCK)
    print df

if __name__ == '__main__':
    STOCK = ['600219',       ##南山铝业
             '000002',       ##万  科Ａ
             '000623',       ##吉林敖东
             '000725',       ##京东方Ａ
             '600036',       ##招商银行
             '601166',       ##兴业银行
             '600298',       ##安琪酵母
             '600881',       ##亚泰集团
             '002582',       ##好想你
             '600750',       ##江中药业
             '601088',       ##中国神华
             '000338',       ##潍柴动力
             '000895',       ##双汇发展
             '000792']       ##盐湖股份

    get_all_price(STOCK)