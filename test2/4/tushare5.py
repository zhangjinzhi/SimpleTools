# -*- coding:utf-8 -*-
import tushare as ts
#通联数据的开发者token
ts.set_token('7cdd10b4b704379a72a9cb60396d1e5f00f12e1587a7f8df8adaa9d640400d5a')
#print ts.get_token()

bd = ts.Fundamental()
df = bd.FdmtBS(ticker='600848', field='ticker,TCA,fixedAssets,inventories,intanAssets')
print df