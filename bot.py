# -*- coding: utf-8 -*-
import itchat
from itchat.content import *

groupChat = {'STAT400':'STAT400 SP18',
'STAT420':'STAT 420 SP18',
'STAT410':'SP18 STATS 410',
'MATH444':'18Spring Math444',
'MATH441':'18spring math441',
'MATH415':'SP2018 MATH415',
'MATH416':'MATH 416 SP2018',
'CS125':'CS125 SP18',
'CS241':'CS241 2018SP',
'CS374':'CS374 SP18',
'CS411':'CS411 18SP',
'CS440':'CS440 SP18',
'CS425':'CS425 SP18',
'CHEM104':'Spring 2018 Chem 104',
'PHYS212':'PHYS212 18Spring',
'ECE110':'ECE110 SP18',
'PHYS211':'PHYS211 sp2018',
'MATH347':'spring2018 math 347',
'MATH241': 'MATH241 sp2018',
'CS173':'CS173 sp2018',
'ART103': 'ART103 sp2018',
'CS225':'CS225 SP18',
'CS126':'cs126 2018 spring',
'ECE120':'ECE120 SP18',
'ESL115':'18sp esl115',
'CS233': 'CS233 SP18',
'MATH231':'MATH231 SP2018',
'ECON203':'ECON203 SP18',
'CS461':'CS461 SP18',
'ACCY202':'ACCY202 SP18',
'BADM320':'BADM320 SP18',
'ECON102':'ECON102 SP18',
'ECON202':'ECON202 SP2018',
'ECON103':'econ103 sp18',
'CS438':'CS438 SP18',
'PHYS213':'PHYS213 SP18',
'PHYS214':'PHYS214 SP18',
'CS357':'CS357 SP18',
'ANSC250':'ANSC250 SP18',
'CS410':'CS410 18SP',
'FIN221':'FIN221 SP18',
'ECON302':'ECON302 SP18',
'ECON303':'ECON303 SP18',
'CS105':'CS105 SP2018',
'CS418':'CS418 SP18',
'PSYC100':'PSYC100 SP18',
'STAT430':'Stat430 StochasticProcesses SP18',
'INFO490':'INFO490 Advanced SP18',
'STAT100':'stat100 sp18',
'MATH234':'MATH234 SP18',
'STAT200':'STAT200 SP18',
'ADV150':'ADV150 SP18',
'MATH285':'SP2018 MATH285',
'CS101':'CS101 SP18',
'STAT431':'Stat 431 SP18',
'STAT432':'Stat 432 SP18',
'BADM300':'Badm300 SP2018',
'PSYC201':'Psyc201 SP18',
'ECE385':'ECE385 SP18',
'CS543':'CS543 SP18',
'ECE391':'ECE 391 SP18',
'STAT426':'Stat 426 SP18',
'CMN101':'CMN101 SP18',
'STAT440':'STAT440 SP18',
'CS398CC':'CS 398 CC SP18',
'CHEM436':'chem 436 437',
'CHEM437':'chem 436 437',
'STAT428':'Stat 428 SP18',
'CS421':'CS421 18SP',
'MATH413':'Math413 SP18',
'ACCY201':'SP2018 ACCY201',
'CS412':'CS412 SP18',
'CS498AML':'CS498AML SP18',
'ECE313':'ECE313 SP18',
'ECE329':'ECE329 SP18',
'CPSC116':'CPSC116 SP2018',
'ATMS120':'atms120 SP18',
'THEA101':'THEA 101 SP18 Online',
'ECE220':'ECE220 SP2018',
'MATH286':'MATH 286 SP2018',
'CHEM102':'CHEM102 103 SP18',
'CHEM103':'CHEM102 103 SP18',
'DANC100':'DANC100 SP18',
'MUS133':'MUS133 SP18',
'ECE210':'ECE210 SP2018',
'FSHN101':'FSHN101 SP18',
'ANTH101':'ANTH101 SP18',
'FSHN232':'fshn232 SP18',
'CLCV115':'CLCV115 SP18',
'LING111':'LING111 18SP',
'ECE310':'ECE310 SP18',
'MATH220':'MATH220 Sp18',
'BADM310':'BADM310 SP18',
'CS446':'CS446 SP18',
'MATH124':'Math124 sp18',
'MATH210':'Math210 SP18',
'MCB150':'MCB150 SP18',
'MATH408':'Math408 SP18',
'TAM210':'TAM210 211 SP18',
'TAM211':'TAM210 211 SP18',
'PHIL102':'phil102 sp18',
'MATH417':'MATH417 SP18',
'CS498VR':'CS498VR SP18',
'MATH453':'math453 SP18',
'HIST100':'HIST100 SP18',
'PHIL110':'REL PHIL 110 SP18',
'REL110':'REL PHIL 110 SP18',
'MCB250':'MCB250 SP18',
'SOC100':'SOC100 SP18',
'PHYS325':'PHYS325 SP18',
'FSHN120':'FSHN120 SP18',
'ECON471':'ECON471 SP18',
'MATH482':'MATH482 SP18',
'CS210':'CS210 SP2018',
'MACS101':'Macs101 SP18',
'SHS120':'SHS120 SP18',
'CPSC131':'CPSC131 SP18',
'FIN300':'SP 18 FIN 300',
'CS465':'CS465 SP18',
'INFO102':'Info102'
}
'''
groupChat = {'CHEM102':'CHEM102 17Fall',
    'CHEM232':'Chem 232',
    'ECON203':'Econ203Fall17',
    'MATH241':'MATH241 17Fall',
    'ECON103':'Econ103',
    'CS125':'CS 125 2017',
    'MATH231':'MATH231 17Fall',
    'PHYS211':'PHYS211 17Fall',
    'MATH220':'MATH220 17Fall',
    'ECON102':'Econ 102 Fall2017',
    'CS233':'Fall2017 CS233',
    'CS173':'CS173 FA17',
    'CS241':'CS 241 FA2017',
    'ACCY201':'Accy201 Fall17',
    'STAT400':'STATS400 FA17',
    'PHYS214':'PHYS214 17Fall',
    'PHYS213':'PHYS213 17Fall',
    'PHYS212':'PHYS212 17Fall',
    'MATH221':'MATH221 17Fall',
    'FIN221':'Fin221 Fall17',
    'CS225':'CS225 FA17',
    'BADM310':'BADM310 17Fall',
    'CS357':'CS 357',
    'CS411':'CS411',
    'ECE110':'ECE110',
    'ECE210':'ECE 210',
    'CS101':'CS101',
    'MATH415':'MATH415',
    'MATH416':'Math416',
    'MATH447':'math447',
    'PSYC201':'psyc201',
    'STAT200':'stat200',
    'DANC100':'Danc100',
    'MCB150':'MCB 150',
    'STAT100':'stat100',
    'PHIL102':'PHIL102',
    'CHEM104':'Chem 104',
    'THEA101':'Thea101',
    'ACCY202':'ACCY202',
    'ME300':'ME300',
    'TAM212':'Tam212',
    'MACS356':'MACS356',
    'MATH447':'math447',
    'MATH347':'MATH 347H',
    'TAM211':'TAM 211',
    'STAT420':'STAT420',
    }
'''
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    #itchat.add_friend(**msg['Text'])
    itchat.send_msg('你好!我是抢课王负责拉群的小助手!输入\"群聊\"获取现有群聊列表，或者直接输入课名让小助手拉你入群(eg:CS125)', msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    if msg['Text'] == '群聊':
        return (u'微信群列表如下：\n' + '\n'.join(sorted(groupChat.keys())) + u'\n输入课名让小助手拉你入群(eg:CS125)')
    if msg['Text'].replace(' ','').upper() in groupChat.keys():
        return add_group(msg['FromUserName'],groupChat[msg['Text'].upper().replace(" ","")])
    if '抢课' in msg['Text']:
        return u'请关注公众号"抢课王"抢课，俺是一个负责拉群的小机器人'
    if '你好' in msg['Text']:
        return u'你好哟～'
    if '谢谢' in msg['Text']:
        return u'不谢'
    if '感谢' in msg['Text']:
        return u'不谢'
    else:
        return u'不存在此群聊\n请直接输入课名让小助手拉你进群(eg.CS125)\n输入“群聊”查看现在支持的群聊列表'

def add_group(userID, groupChatName):

    itchat.send_msg('等着 俺给你拉群里',userID)
    chatrooms = itchat.search_chatrooms(name=groupChatName)

    #r = itchat.update_chatroom(chatrooms[0]['UserName'],detailedMember=True)
    #if r['MemberCount'] < 90:
        #return 'not over 90 yet,, plz use QKW!'

    friend = itchat.search_friends(userName=userID)
    res = itchat.add_member_into_chatroom(chatrooms[0]['UserName'],[friend],useInvitation=True)

    if res["BaseResponse"]["Ret"]:
        itchat.send_msg('系统更新中QuQ 请稍后重试',userID)


itchat.auto_login(enableCmdQR=2)
itchat.run()
