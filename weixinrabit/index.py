# coding=utf8
import itchat
import random, time
import os, re
from weixinrabit.wxtools import wxTools, wxMsgManager, wxUserInfo, wxGroupInfo, wxConfigSingleton
from apscheduler.schedulers.blocking import BlockingScheduler

msg_dict = {}
face_bug = None

# 好友/群-文本消息
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=True)
def text_msg(msg):
    global face_bug
    # 不是自己发送的消息，收到的信息
    if msg['FromUserName'] != wxConfigSingleton.WXConfigSingleton().my_user_name:
        # 判断为群聊,为接收到的消息
        if '@@' in msg['FromUserName']:
            # 群中有人找小艾同学
            if wxTools.isCallMe(msg):
                try:
                    defaultReply = '我现在只想模仿你:' + msg['Text']
                    # 在测试的发现他是无关政治，我想这句我要加上
                    if '台湾' in msg['Text']:
                        return '台湾是中国不可分割的一部分,支持祖国收复台湾,建立台湾省'

                    reply = wxMsgManager.get_response(msg['Text'])
                    # 更新聊天数据
                    wxTools.updateMessage(msg_dict, msg)
                    return reply or defaultReply
                except Exception as error:
                    print(error)
                    return
        else:  # 判断为个人消息, 为接收到的消息
            # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
            try:
                defaultReply = '我现在只想模仿你:' + msg['Text']
                # 在测试的发现他是无关政治，我想这句我要加上
                if '台湾' in msg['Text']:
                    return '台湾是中国不可分割的一部分,支持祖国收复台湾,建立台湾省'
                reply = wxMsgManager.get_response(msg['Text'])
                # 更新聊天数据
                wxTools.updateMessage(msg_dict, msg)
                # return reply or defaultReply

                # 从小冰获取回复消息
                face_bug = msg['FromUserName']
                mp_info = wxGroupInfo.getMpsInfoWithGroupName('小冰')
                itchat.send(msg['Text'], toUserName=mp_info['UserName'])
            except Exception as error:
                print(error)
                return
    else:
        cmd_dic = {
            '/开启回复': '自动回复已开启',
            '/关闭回复': '自动回复已关闭',
            '/配置': '@fil@conf/reply.xls',
            '/帮助': '/帮助  显示帮助信息\n\n/配置  下载服务端配置文件\n\n群发:x\nx为纯数字,下一条消息将被转发到配置的群分组\n\n/开启回复  开启自动回复\n\n/关闭回复  关闭自动回复',
        }
        if msg['Text'] == '/开启回复':
            wxConfigSingleton.WXConfigSingleton().auto_reply = True
        if msg['Text'] == '/关闭回复':
            wxConfigSingleton.WXConfigSingleton().auto_reply = False
        itchat.send(cmd_dic[msg['Text']], toUserName='filehelper')



# 好友/群-图片消息
@itchat.msg_register(itchat.content.PICTURE, isFriendChat=True, isGroupChat=True)
def image_msg(msg):
    # 不是自己发送的消息，收到的信息
    if msg['FromUserName'] != wxConfigSingleton.WXConfigSingleton().my_user_name:
        try:
            defaultReplay = 'I love picture'
            # 以下方法会下载文件
            path = './images/'  # 图片路径
            dirs = os.listdir(path)
            # 保存图片
            # wxTools.saveImageToImages(msg)
            typeSymbol = {'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil')
            reply = '@%s@%s' % (typeSymbol, path + random.choice(dirs))
            # 更新聊天数据
            wxTools.updateMessage(msg_dict, msg)
            time.sleep(random.randint(1, 2))
            return reply or defaultReplay

        except Exception as error:
            print(error)
            return


# 好友/群-视频消息
@itchat.msg_register([itchat.content.VIDEO], isFriendChat=True, isGroupChat=True)
def friend_video_msg(msg):
    # 不是自己发送的消息，收到的信息
    if msg['FromUserName'] != wxConfigSingleton.WXConfigSingleton().my_user_name:
        # 更新聊天数据
        wxTools.updateMessage(msg_dict, msg)
        # return '有人发视频'
        try:
            defaultReplay = 'I love picture'
        #     # 以下方法会下载文件
        #     path = './images/'  # 图片路径
        #     dirs = os.listdir(path)
        #     # 保存图片
            #wxTools.saveImageToImages(msg)
        #msg['Text'](msg['FileName'])
            typeSymbol = {'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil')
            reply = '@fil@190612-183933.mp4'
        #     # 更新聊天数据
        #     wxTools.updateMessage(msg_dict, msg)
        #     # 发送消息
            time.sleep(random.randint(1, 2))
            itchat.send_video('190612-183933.mp4', toUserName=msg['FromUserName'])

            # return reply or defaultReplay
        except Exception as error:
            print(error)
            return


'''
  收到好友邀请自动添加好友
'''
@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    # msg.user.verify()
    #msg.user.send('Nice to meet you!')
    itchat.send_msg('Nice to meet you ^_^', msg['RecommendInfo']['UserName'])


'''
  监听小组分享连接消息
'''
@itchat.msg_register(itchat.content.SHARING, isFriendChat=True, isGroupChat=True)
def group_share_replay(msg):
    print('d')
    return msg['Url']



'''
  监听公众号信
'''
@itchat.msg_register(itchat.content.TEXT, isMpChat=True)
def reply_msg(msg):
    global face_bug
    mp_info = wxGroupInfo.getMpsInfoWithGroupFromName(msg['FromUserName'])
    print("收到一条公众号信息：", mp_info['NickName'], msg['Content'])
    itchat.send(msg['Content'], toUserName=face_bug)

'''
  消息撤回
'''
@itchat.msg_register([itchat.content.NOTE], isFriendChat=True, isGroupChat=True)
def revoke_msg(msg):
    rev_tmp_dir = './temps/'
    if re.search(r"\<\!\[CDATA\[.*撤回了一条消息\]\]\>", msg['Content']) is not None:
        # 获取消息的id
        old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
        old_msg = msg_dict.get(old_msg_id, {})
        if len(old_msg_id) < 11:
            itchat.send_file(rev_tmp_dir + face_bug, toUserName='filehelper')
            os.remove(rev_tmp_dir + face_bug)
        else:
            msg_body = "告诉你一个秘密~" + "\n" \
                       + old_msg.get('msg_from') + " 撤回了 " + old_msg.get("msg_type") + " 消息" + "\n" \
                       + old_msg.get('msg_time_rec') + "\n" \
                       + "撤回了什么 ⇣" + "\n" \
                       + r"" + old_msg.get('msg_content')
            # 如果是分享存在链接
            if old_msg['msg_type'] == "Sharing": msg_body += "\n就是这个链接➣ " + old_msg.get('msg_share_url')

            # 将撤回消息发送到文件助手
            itchat.send(msg_body, toUserName='filehelper')
            # 有文件的话也要将文件发送回去
            if old_msg["msg_type"] == "Picture" \
                    or old_msg["msg_type"] == "Recording" \
                    or old_msg["msg_type"] == "Video" \
                    or old_msg["msg_type"] == "Attachment":
                file = rev_tmp_dir + old_msg['msg_content']
                itchat.send('@fil@%s' % file, toUserName='filehelper')
                #itchat.send(file, toUserName='filehelper')
                #os.remove(rev_tmp_dir + old_msg['msg_content'])
            # 删除字典旧消息
            msg_dict.pop(old_msg_id)


'''
  用户多开
'''
# @newInstance.msg_register(itchat.content.TEXT)
# def reply(msg):
#     return msg.text

'''
  用户多开方法
'''
def multipUser():
    newInstance = itchat.new_instance()
    newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')
    newInstance.run()

# 发送信息
def send_msg():
    user_info = itchat.search_friends(name='培杰')
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        itchat.send_msg('生日快乐哦！', toUserName=user_name)


'''
  登录后调用
'''
def after_login():
    print("登录后调用")
    # 开启轮询
    #sched.add_job(send_msg, 'cron', year=2018, month=7, day=28, hour=16, minute=5, second=30)
    #sched.start()

'''
  退出后调用
'''
def after_logout():
    print("退出后调用")
    # 关闭轮询
    #sched.shutdown()
    wxTools.removeTempConfig()

'''
  初始化默认配置
'''
def initConfig():
    # 文件存储临时目录
    wxTools.removeTempConfig()
    wxTools.initTempConfig()
    # 获取我的id
    wxConfigSingleton.WXConfigSingleton().my_user_name = wxUserInfo.getUserInfoOfMe().user_name


'''
  修改程序不用多次扫码,我们使用热启动
'''
if __name__ == '__main__':
    # sched = BlockingScheduler()
    itchat.auto_login(hotReload=True, loginCallback=after_login, exitCallback=after_logout)
    #itchat.send('@img@%s' % "./images/190611-153938.png", toUserName='filehelper')
    # itchat.send('@fil@%s' % "./index.py", toUserName='filehelper')

    # itchat.send('@img@%s' % "./images/181203-175233.gif", toUserName='filehelper')
    # itchat.send_msg('ddd', toUserName='filehelper')
    # itchat.send_image(os.getcwd()+"/images/190611-153938.png", toUserName='filehelper')
    # 初始化默认配置
    initConfig()
    # itchat.send('@vid@%s' % './temps/190612-165953.mp4', toUserName='filehelper')
    #fileexist =itchat.send_video('aa4e76876465435ca7a8be3c2b2beab0.mp4', toUserName='filehelper')
    itchat.run(debug=True)


