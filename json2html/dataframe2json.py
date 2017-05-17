#coding:utf-8
import tushare as ts
from json2html import *
import pandas

result =ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')

print result
print "///////////////////////////////////////////////////"
print result.T


input1 = result.to_json()
print input1
print "///////////////////////////////////////////////////"
input2 =  result.T.to_json()
print input2


html1 = json2html.convert(json= input1)
with open("origin.html",'wb') as f:
    f.write(html1.encode('utf-8'))

html2 = json2html.convert(json= input2)
with open("changed.html",'wb') as f:
    f.write(html2.encode('utf-8'))