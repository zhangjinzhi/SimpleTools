# -*- coding:utf-8 -*-
import tushare as ts

#df=ts.get_industry_classified()
#df.to_csv('industryClassified.csv')
#print ts.get_concept_classified()
#print ts.get_area_classified()
#print ts.get_sme_classified()

#print ts.get_terminated()
#print ts.get_suspended()

#df = ts.get_hist_data('000875')
#直接保存
#df.to_csv('000875.csv')
#df.to_csv('000875partial.csv',columns=['open','high','low','close'])

#
# import os
#
# filename = 'severalStocks.csv'
# for code in ['000875', '600848', '000981']:
#     df = ts.get_hist_data(code)
#     if os.path.exists(filename):
#         df.to_csv(filename, mode='a', header=None)
#     else:
#         df.to_csv(filename)

# df = ts.get_hist_data('000875')
# df.to_hdf('hdf.h5','000875')

# df = ts.get_hist_data('000875')
# df.to_json('000875.json',orient='records')


from sqlalchemy import create_engine

df = ts.get_tick_data('000981', date='2014-12-22')

engine = create_engine('mysql://root:zjz4818774@127.0.0.1/tushare?charset=utf8')  #数据库名

#存入数据库
df.to_sql('tick_data1',engine)  #表名

#追加数据到现有表
#df = ts.get_hist_data('000875')
#df.to_sql('tick_data2',engine,if_exists='append')