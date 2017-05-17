# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import DataAPI        #通联数据平台提供的API
                      #  http://tushare.org/index.html#id5
                     # https://uqer.io/community/share/57fce2b0228e5b3668facaf0?source=home
                    #http://www.36dsj.com/archives/51828
bdt="20160311" #期间开始
edt="20161011" #期间结束


themeName =u'锂电池'
#获取某主题相关股票的信息
ztid=DataAPI.TickersByThemesGet(themeID=u"",themeName=themeName,beginDate=u"",endDate=u"",isNew=u"",field=u"",pandas="1")
gpjc=ztid.secShortName.tolist() #股票简称
stocklist=ztid.secID.tolist() #股票代码
returnall=[] #设立收益列表
mrktval1=[]
mrktval2=[]
ysdf=pd.DataFrame()
#print(stocklist)
#获取股票list中的各股票收益并装入returnall中
for i in stocklist:
    price1=DataAPI.MktEqudAdjGet(secID=i,\
                             beginDate=bdt,endDate=bdt,field=u"secID,closePrice",pandas="1")#期间开始价格
    price2=DataAPI.MktEqudAdjGet(secID=i,\
                             beginDate=edt,endDate=edt,field=u"secID,closePrice,negMarketValue,marketValue",pandas="1")#期间结束价格
    returnget=round(float(price2.closePrice[0]/price1.closePrice[0]-1),4)#收益，保留四位小数
    returnget1=str(returnget*100)+'%'
    returnall.append(returnget1)
    mrktval1.append(int(price2.negMarketValue/100000000))
    mrktval2.append(int(price2.marketValue/100000000))
#print mrktval1
indexlen=len(stocklist)+1#为了设置Index
alltable=pd.DataFrame(np.array(zip(stocklist,gpjc,returnall)),columns=['代码','股票简称','期间涨幅'])#index=list(range(1,indexlen))

alltable1=alltable.join(pd.Series(mrktval1,name='流动市值'))
alltable2=alltable1.join(pd.Series(mrktval2,name='总市值'))


alltable2