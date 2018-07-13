# -*- coding: utf-8 -*-

'''
  Created on Tue Jun 26 2017

  @author Hetian Huo, Vivian Hu
  Copyright (c) 2018 Coursely

'''

import itchat
from itchat.content import *
import chatGroup

groupChat = chatGroup.groupChat

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.send_msg('你好!我是抢课王负责拉群的小助手!输入\"群聊\"获取现有群聊列表，或者直接输入课名让小助手拉你入群(eg:CS125)', 
                    msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    if msg['Text'] == '群聊':
        return (u'微信群列表如下：\n' + '\n'.join(sorted(groupChat.keys())) + u'\n输入课名让小助手拉你入群(eg:CS125)')
    if msg['Text'].replace(' ','').upper() in groupChat.keys():
        return add_group(msg['FromUserName'], groupChat[msg['Text'].upper().replace(" ","")])
    if '抢课' in msg['Text']:
        return u'请关注公众号"抢课王"抢课，俺是一个负责拉群的小机器人'
    if '你好' in msg['Text']:
        return u'你好哟～'
    if '谢谢' in msg['Text']:
        return u'不谢'
    else:
        return u'不存在此群聊\n请直接输入课名让小助手拉你进群(eg.CS125)\n输入“群聊”查看现在支持的群聊列表'

def add_group(userID, groupChatName):
  
    itchat.send_msg('等着 俺给你拉群里',userID)
    chatrooms = itchat.search_chatrooms(name=groupChatName)

    friend = itchat.search_friends(userName=userID)
    res = itchat.add_member_into_chatroom(chatrooms[0]['UserName'], [friend], useInvitation=True)

    if res["BaseResponse"]["Ret"]:
        itchat.send_msg('系统更新中QuQ 请稍后重试', userID)

itchat.auto_login(enableCmdQR=2)
itchat.run()
