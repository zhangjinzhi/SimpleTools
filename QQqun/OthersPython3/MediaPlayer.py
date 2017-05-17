#coding:utf-8
from tkinter import *
import tkinter.messagebox
import re,time
import urllib
import urllib2.Request
import urllib.parse
import urllib
import urllib2
import requests
import json
import mp3play

def music():
    word=entry.get().encode('utf-8')
    if not word:
        tkinter.messagebox.showinfo('提示','嘿，愚蠢的人类，赶快输入歌名')
        return
    else:
        word=urllib.parse.quote(word)
        word.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
        html=urllib2.Request.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=9' %word).read()
        html=html.decode('utf-8')
        js=json.loads(html)
        sy=0
        for i in js['result']['songs']:
            listbox.insert(sy,i['name']+i['artists'][0]['name'])

def clear():
    listbox.delete(0,listbox.size())
    var.set('')

def play(event):
    pl=listbox.curselectiion()[0]
    audio=sy[pl]['audio']
    urllib.urlretrieve(audio,'music.mp3')
    mp3=mp3play.load('music.mp3')
    mp3.play
    mp3.second(time,sleep(300))
    mp3.stop()
    print(pl)

root=Tk()
root.geometry('450x250')
root.title('简单粗暴播放器')
entry=Entry(root)
entry.pack()

Button(root,text='搜 索',command=music).pack()
button2=Button(root,text='清空',command=clear)
button2.pack()

var=StringVar()
listbox=Listbox(root,width=50,listvariable=var)
listbox.pack()
Label(root,text='简单粗暴',fg='red').pack()
root.mainloop()
