# -*- coding:utf-8 -*-

import re
import time
import requests
from PIL import Image


url_login = 'https://www.zhihu.com/login/phone_num'

headers = {
        'Host' : 'www.zhihu.com',
        'Origin' : 'https://www.zhihu.com',
        'Referer' : 'https://www.zhihu.com/',
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

session = requests.session()

# 获取xsrf
def get_xsrf():
    url = 'https://www.zhihu.com/#signin'
    html = session.get(url)
    pageCode = html.text
    pattern = re.compile('name="_xsrf" value="(.*?)"/>',re.S)
    xsrf = re.search(pattern,pageCode).group(1)
    return xsrf

# 获取验证码
def get_captcha():
    # 获取验证码url
    t = str(int(time.time() * 1000))
    url = 'http://www.zhihu.com/captcha.gif?r=%s&type=login' % t
    cha = session.get(url)
    with open('cha.jpg', 'wb') as f:
        f.write(cha.content)
        f.close()
        im = Image.open('cha.jpg')
        im.show()
        im.close()
    captcha = raw_input("请输入验证码")
    return captcha


form_data = {
        '_xsrf' : get_xsrf(),
        'password' : 'ChelseaFC.1',
        'captcha' : get_captcha(),
        'remember_me' : 'true',
        'phone_num' : '18362972928'
}
print form_data
# 注意用法
res = session.post(url_login,data=form_data,headers=headers)
print res.json()['msg']