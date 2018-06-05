import itchat

_keywords_no_play = ['小猪', '德扑', '小朱', '打牌']
_keywords_play = ['斗地主']

wechatGroupList = ['早饭要吃蛋', '一杯敬宝强 一杯敬乃亮']

@itchat.msg_register(itchat.content.TEXT, isGroupChat = True)
def group_reply(msg):
    fromUserName = msg['FromUserName'];
    group = itchat.search_chatrooms(userName = fromUserName)
    groupName = group['NickName']
    print(groupName)
    if group['NickName'] not in wechatGroupList:
        return
    message = getText(msg)
    if msg['isAt']:
        sendMessage('？', msg['FromUserName'])
    if match(message, _keywords_no_play):
        print("触发--------------no_play")
        sendMessage('有事不打',msg['FromUserName'])
    if match(message, _keywords_play):
        print("触发--------------play")
        sendMessage('斗地主可以', msg['FromUserName'])

def getText(msg):
    if msg['Type'] == 'Text':
        return msg['Text']
    else:
        return "其他类型"

def match(msg, keywords_list):
    for kw in keywords_list:
        if kw in msg:
            return True
    return False

def sendMessage(msg, name):
    itchat.send_msg(msg, toUserName = name)

itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
