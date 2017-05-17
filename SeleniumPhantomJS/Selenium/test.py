#coding:utf-8

from selenium import webdriver
import time
def main():

    chromeDriverDir = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    b = webdriver.Chrome(executable_path=chromeDriverDir)        # 打开 Chrome 浏览器

   # b=webdriver.Chrome()
    b.get('http://www.baidu.com')
    time.sleep(5)
    b.quit()

if __name__ == '__main__':
    main()