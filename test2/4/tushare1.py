# -*- coding: utf-8 -*-

############################http://tushare.org/storing.html##官网！！！！！！！！！！！！！！！
import tushare as ts

print  ts.__version__

print ts.get_stock_basics()

from sqlalchemy import create_engine

import tushare as ts

df = ts.get_tick_data('600848',date='2014-12-22')

engine = create_engine('mysql+mysqldb://root:zjz4818774@127.0.0.1/tushare?charset=utf8')

#存入数据库

df.to_sql('tick_data',engine)