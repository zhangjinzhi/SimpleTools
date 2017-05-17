#coding:utf-8
import pandas as pd
import pandas.io.data as web
from pandas_datareader import data, wb
import datetime

start = datetime.datetime(2016,1,1)
end = datetime.date.today()
#用pandas可以直接从雅虎财经谷歌等上直接获取股票信息，不过得安装pandas的扩展模块
apple = web.DataReader("APPLE","yahoo",start,end)

type(apple)
