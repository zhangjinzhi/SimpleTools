# -*- coding: utf-8 -*-

############################http://tushare.org/storing.html##官网！！！！！！！！！！！！！！！
import tushare as ts
import numpy as np

print  ts.__version__

from sqlalchemy import create_engine
import tushare as ts
import pandas as pd
df=ts.get_h_data('002337') #前复权
print df


frame = pd.DataFrame(df,columns=['time','open','close','low','high'])
time = frame.index
frame['time'] = time
print frame
result = frame.values


#np.savetxt("tyshare6.txt", result, fmt="%s")
#print result

#print frame.index
# print frame['open']
# print frame['close']
# print frame['low']
# print frame['high'].values
#engine = create_engine('mysql://root:zjz4818774@127.0.0.1/tushare?charset=utf8')
#
# #存入数据库
#
#df.to_sql('tick_data6',engine)