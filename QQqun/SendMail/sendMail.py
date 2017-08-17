# -*- coding:utf-8 -*-
#确少SMTP设置#################################################
import smtplib

from email.mime.text import MIMEText

mail_list = ["1666925105@qq.com",] #收件箱
mail_host = "smtp.exmail.qq.com"  #邮件服务器
mail_username = "584392383@qq.com"#发件箱
mail_password = ""  #密码

def send_mail(text,to_mail):
    my = "python发邮件测试" + "<" + mail_username + ">"
    msg = MIMEText(text,_subtype="html",_charset="utf-8")
    msg['To'] = ';'.join(to_mail)
    msg['From'] = my
    msg['Subject'] = "你好" #邮件主题
    try: #异常捕获，出错后抛出异常
        server = smtplib.SMTP() #实例化对象保存到s里面
        server.connect(mail_host) #连接欸发信服务器
        server.login(mail_username,mail_password)#登陆邮件服务器
        server.sendmail(my,to_mail,msg.as_string())#发送邮件
        server.close()
        return True
        print '完成'
    except Exception,e:
        print '发送错误'
        print str(e)
        return False


if __name__ == '__main__':
    text = "<a>我是python做的假邮件</a>"
    if send_mail(text,mail_list):
         print "发送成功"
    else:
       print "发送失败"
