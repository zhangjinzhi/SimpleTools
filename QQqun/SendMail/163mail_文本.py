# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
import smtplib

#发件人列表
mail_to_list=["1359980618@qq.com","584392383@qq.com"]
#对于大型的邮件服务器，有反垃圾邮件的功能，必须登录后才能发邮件，如126,163
mail_server="smtp.163.com"         # 126的邮件服务器
mail_username="18202723109@163.com"   #必须是真实存在的用户，这里我测试的时候写了自己的126邮箱
mail_passwd="zhang4818774"               #必须是对应上面用户的正确密码，我126邮箱对应的密码

def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me = "张金志" + "<" + mail_username + ">"
    #msg = MIMEText(content)
    msg = MIMEText(content,_subtype='plain',_charset="utf-8")
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_server)
        s.login(mail_username,mail_passwd)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    subject = "单娜姑娘，我是小志"
    text = "我是python做的邮件"
    if send_mail(mail_to_list,subject,text):
        print "发送成功"
    else:
        print "发送失败"