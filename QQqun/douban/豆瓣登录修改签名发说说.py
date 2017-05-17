# -*- coding:utf-8 -*-

import re
import time
import requests
from PIL import Image

url = 'https://www.douban.com/'

headers = {
        'origin' : 'https://www.douban.com',
        'referer' : 'https://www.douban.com/',
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

session = requests.session()

# 获取验证码Id
def get_captchaId():
    html = session.get(url,headers=headers)
    html.encoding = 'utf-8'
    pageCode = html.text
    pattern = re.compile('captcha[?]id=(.*?)&',re.S)
    captchaId = re.findall(pattern,pageCode)[0]
    return captchaId

# 获取验证码图片
def get_captchaSolu(captchaId):
    url_plus = 'https://www.douban.com/misc/captcha?id=%s&size=s' % captchaId
    cha = session.get(url_plus,headers=headers)
    with open('cap_douban.png','wb') as f:
        f.write(cha.content)
        f.close()
        im = Image.open('cap_douban.png')
        im.show()
        im.close()
    captcha = raw_input('请输入验证码')
    return captcha

# 编辑签名
def edit_signature(ck):
    url = 'https://www.douban.com/j/people/143780683/edit_signature'
    data = {
        'ck' : ck,
        'signature' : '人间有味是清欢。'
    }
    headers = {
            'origin' : 'https://www.douban.com',
            'referer' : 'https://www.douban.com/people/143780683/',
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'x-requested-with' : 'XMLHttpRequest'
    }
    session.post(url,data=data,headers=headers)

# 编辑说说
def edit_words(ck):
    url = 'https://www.douban.com/'
    data = {
        'ck' : ck,
        'comment' : '天之涯，地之角，知交半零落。一斛浊酒尽余欢，今宵别梦寒。'
    }
    headers = {
        'origin': 'https://www.douban.com',
        'referer': 'https://www.douban.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
    }
    session.post(url,data=data,headers=headers)

# 获取ck
def get_ck():
    url = 'https://www.douban.com/people/143780683/'
    html = session.get(url,headers=headers)
    pageCode = html.text
    # print pageCode
    pattern = re.compile('ck=(.*?)[(">)]',re.S)
    ck = re.findall(pattern,pageCode)[0]
    return ck

if __name__ == '__main__':
    captchaId = get_captchaId()
    captcha = get_captchaSolu(captchaId)
    form_data = {
            'source' : 'index_nav',
            'form_email' : '18362972928',
            'form_password' : 'ChelseaFC.2',
            'captcha-solution' : captcha,
            'captcha-id' : captchaId
    }
    session.post('https://www.douban.com/accounts/login',data=form_data,headers=headers)

    ck = get_ck()
    edit_signature(ck)
    # 避免冲突，设置延时
    time.sleep(5)
    edit_words(ck)