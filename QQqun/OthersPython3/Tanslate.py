# -*- coding:utf8 -*- #编码
import urllib2.parse
import urllib
import urllib2
import requests
import json
from tkinter import *
import tkinter.messagebox


def en():#定义函数
    global word
    word=entry.get().encode('utf8')

    if not word:
        tkinter.messagebox.showinfo('提示','嘿，-------愚蠢的人类-------，赶快输入')
        return
    else:
        word=urllib.parse.quote(word)
        return word
def clear():
    lb.delete(0,lb.size())
    return
word=entry.get().encode('utf8')

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index' #有道地址
root=tkinter.Tk()                                    #窗口
root.geometry('450x300')
root.title('简单粗暴翻译')
Button(root,text='翻 译',command=en).pack()
Button(root,text='清 空',command=clear).pack()
entry=Entry(root)
entry.pack()
lb=Listbox(root,width=50)
lb.pack()
Label(root,text='简单粗暴\n在第一个方框内输入，第二个方框得到结果',fg='red').pack()

data={} #模拟浏览器
data['type']='AUTO'
data['i']=word
data['doctype']='json'
data['xmlVersion']='1.8'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['action']='FY_BY_CLICKBUTTON'
data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')

res=urllib.request.urlopen(url,data)
ht=res.read().decode('utf8')
ht=json.loads(ht)
ht=ht['translateResult'][0][0]['tgt']
lb.insert(0,ht)

mainloop() #循环尾

