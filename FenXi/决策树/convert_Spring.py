# coding=utf-8   #默认编码格式为utf-8

s = u'中文' #unicode编码的文字
print s.encode('utf-8')   #转换成utf-8格式输出
print s #效果与上面相同，似乎默认直接转换为指定编码

u=u'unicode编码文字'
g=u.encode('gbk') #转换为gbk格式
print g #此时为乱码，因为当前环境为utf-8,gbk编码文字为乱码
str=g.decode('gbk').encode('utf-8')   #以gbk编码格式读取g（因为他就是gbk编码的）并转换为utf-8格式输出
print str #正常显示中文

with open("weather_number.txt","w") as f1:
    f=file("weather.txt")
    for i in f:
        strs= i.decode('gbk').encode('utf-8')
        if "雨" in strs:
            b = "-1"
            b += "\n"
            f1.write(b)
        elif "雪" in strs:
             c = "-1"
             c += "\n"
             f1.write(c)
        else:
           a = "1"
           a += "\n"
           f1.write(a)
f1.close()
f.close()



'''
with open("b.txt","w") as f1:
    f=file("1.txt")
    for i in f:
        strs= i.decode('gbk').encode('utf-8')
        if "转" in strs:
            b = "-1"
            b += "\n"
            f1.write(b)
            print "-1"
        else:
           a = "1"
           a += "\n"
           f1.write(a)
           print "1"
f1.close()
f.close()
'''
'''
f=file("3.txt")
string = " "
for i in f:
    strs= i.decode('gbk').encode('utf-8')
    string += strs
print string
f.close()
'''