# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib

#收件人列表
mail_to_list=["584392383@qq.com","1359980618@qq.com"]
#对于大型的邮件服务器，有反垃圾邮件的功能，必须登录后才能发邮件，如126,163
mail_server="smtp.163.com"         # 126的邮件服务器
mail_username="18202723109@163.com"   #必须是真实存在的用户，这里我测试的时候写了自己的126邮箱
mail_passwd=""               #必须是对应上面用户的正确密码，我126邮箱对应的密码

def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me = "张金志" + "<" + mail_username + ">"

    msg = MIMEMultipart()
    msg['Subject'] = sub    # 邮件主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    txt = MIMEText("刚才那个发错了，我用python重回发一遍，附件是我这几天试验测试的代码，你可以复制粘贴看看，通过结果的不同来体会一下", _subtype='plain', _charset='utf8')
    msg.attach(txt)
    #用下面的代码 ，发送附件就不会显示附件内容，比如不现实图片。因为用了 src="cid:image1"
    # msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<img alt="" src="cid:image1" />good!', 'html', 'utf-8')
    # msg.attach(msgText)
    # file1 = "F:\\1.jpg"
    # image = MIMEImage(open(file1, 'rb').read())
    # image.add_header('Content-ID', '<image1>')
    # msg.attach(image)

#这样写，如果是单个附件，就会将附件的图片显示出来  多个附件的话，也不会将图片显示出来
    att1 = MIMEText(open('1.jpg', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="1.jpg"'
    msg.attach(att1)
    att2 = MIMEText(open('2.jpg', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="2.jpg"'
    msg.attach(att2)
    att3 = MIMEText(open('PycharmProject.rar', 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="PycharmProject.rar"'
    msg.attach(att3)
    try:
         # 加密SMTP
         # smtp_port = 25    # 默认端口号为25
         # s = smtplib.SMTP(mail_server, smtp_port)
         #  s.starttls()
         s = smtplib.SMTP()
         s.connect(mail_server)
         s.login(mail_username,mail_passwd)
         s.sendmail(me, to_list, msg.as_string())
         #s.set_debuglevel(1)     # 打印出和SMTP服务器交互的所有信息
         s.close()
         return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    subject = "我是小志"
    html = "<html></html>"
    if send_mail(mail_to_list,subject,html):
        print "发送成功"
    else:
        print "发送失败"

