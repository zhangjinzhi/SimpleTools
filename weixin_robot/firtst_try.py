import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg['Text']

itchat.auto_login(hotReload=True)
itchat.send('Hello, filehelper', toUserName='filehelper')
itchat.run()