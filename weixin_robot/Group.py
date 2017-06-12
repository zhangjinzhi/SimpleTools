#coding=utf-8
import requests
import itchat
from itchat.content import *

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    '''
	构造图灵机器人返还的数据
	'''
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    reply = get_response(msg['Text'])
    print reply
    return reply

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def print_members_reply(msg):
    if(msg['Text']==u"打印名单"):
        student = ''
        source = msg['FromUserName']
        for i in range(len(itchat.get_contact())):
            if(itchat.get_contact()[i]['UserName']==source):
                user_group = itchat.get_contact()[i]['MemberList']
                for j in range(len(user_group)):
                    student += user_group[j]['NickName'] + '\n'
        itchat.send(student,toUserName=source)



@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)  #为True时自动回复群消息，False时不能回复
def group_text_reply(msg):
    print_members_reply(msg)
    reply = get_response(msg['Text'])
    source = msg['FromUserName']
    username = msg['ActualNickName']
    userid = msg['ToUserName']
    print 'souce: '+source
    print 'username: '+username
    print 'userid: '+userid
    print u'群ID'+itchat.get_contact()[2]['UserName']
    # print itchat.get_chatrooms()
    itchat.send(reply, toUserName=source)
    return reply


# 处理多媒体类消息
# 包括图片、录音、文件、视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    # 把下载好的文件再发回给发送者
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


itchat.auto_login(hotReload=True)

itchat.run()