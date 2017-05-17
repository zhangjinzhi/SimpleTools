# -*- coding:utf-8 -*-

from lxml import etree
from PIL import Image
import requests
import re


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
referer = 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt='

headers = {
        'User-Agent' : user_agent,
        'Host' : 'login.weibo.cn',
        'Origin' : 'http://login.weibo.cn',
        'Referer' : referer
}

session = requests.session()

# 注意URL的选择
url = 'https://login.weibo.cn/login/'
html = session.get(url,headers=headers)
pageCode = html.text
pattern = re.compile('password" name="(.*?)".*?name="vk" value="(.*?)".*?"capId" value="(.*?)"',re.S)
items = re.findall(pattern,pageCode)[0]
password,vk,capId = items
# 上面就依次获得了password_xxxx,vk,capId

cap_url = 'http://weibo.cn/interface/f/ttt/captcha/show.php?cpt=' + items[2]
captcha = session.get(cap_url,headers=headers)
with open('cap.png','wb') as f:
    f.write(captcha.content)
    f.close()
    im = Image.open('cap.png')
    im.show()
    im.close
    cap_code = raw_input('请输入验证码:')


form_data = {
        'mobile' : '18202723109',
        password : 'zjz4818774',
        'code' : cap_code,
        'remember' : 'on',
        'backURL' : 'http%3A%2F%2Fweibo.cn%2F',
        'backTitle' : '微博',
        'tryCount' : '',
        'vk' : vk,
        'capId' : capId,
        'submit' : '登录'
}



session.post(url,data=form_data,headers=headers)

url_logined = 'http://weibo.cn/'
html_2 = session.get(url_logined)
html_2.encoding = 'utf-8'
pageCode_2 = html_2.content
Selector = etree.HTML(pageCode_2)
content = Selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    print text