# -*- coding:utf-8 -*-
#
# author: sunboy_2050
# blog: http://blog.mimvp.com

from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def spider_url_content(url):
    try:
      #  FirefoxDriverDir = "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
      #  browser = webdriver.Firefox(executable_path=FirefoxDriverDir)       # 打开 FireFox 浏览器

        chromeDriverDir = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        browser = webdriver.Chrome(executable_path=chromeDriverDir)        # 打开 Chrome 浏览器

      #  browser = webdriver.Chrome()

        browser.get(url)
        content = browser.find_element_by_id('container')       # 通过标记id 获取网页的内容
        content = content.text

        browser.quit()                      # 关闭浏览器

        print("content: " + content)

    except Exception as ex:
        print("error msg: " + str(ex))

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    spider_url_content(url)