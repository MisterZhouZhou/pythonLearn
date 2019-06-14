# coding=utf8
import itchat
import random, time
import os, re
from weixinrabit.wxtools import wxTools, wxMsgManager, wxUserInfo, wxGroupInfo, wxConfigSingleton
from apscheduler.schedulers.blocking import BlockingScheduler

msg_dict = {}
face_bug = None

'''
   使用小冰进行自动回复
'''
def auto_replayOFXB(msg):
    defaultReply = '我现在只想模仿你:' + msg['Text']
    mp_info = wxGroupInfo.getMpsInfoWithGroupName('小冰')
    time.sleep(random.randint(1, 2))
    wxTools.sendTextMessage(msg_text=msg['Text'] or defaultReply, to_user_name=mp_info['UserName'])

'''
   使用图灵进行自动回复
'''
def auto_replayOFTL(msg):
    defaultReply = '我现在只想模仿你:' + msg['Text']
    reply = wxMsgManager.get_response(msg['Text'])
    time.sleep(random.randint(1, 2))
    wxTools.sendTextMessage(msg_text=reply or defaultReply, to_user_name=msg['FromUserName'])

'''
   给文件助手发送指定命令
'''
def send_filehelper(msg):
    # 给文件助手发消息
    cmd_dic = {
        '/开启自动回复': '自动回复已开启',
        '/关闭自动回复': '自动回复已关闭',
        '/使用小冰': '小冰自动回复已开启',
        '/关闭小冰': '小冰自动回复已关闭',
        '/使用图灵': '图灵自动回复已开启',
        '/关闭图灵': '图灵自动回复已关闭',
        '/开启轮询': '轮询已开启',
        '/关闭轮询': '轮询已关闭',
        '/帮助': '/帮助  显示帮助信息\n\n/配置  下载服务端配置文件\n\n /开启回复  开启自动回复\n\n /关闭回复  关闭自动回复',
    }
    if msg['Text'] == '/开启自动回复':
        wxConfigSingleton.WXConfigSingleton().auto_reply = True
        # 默认使用图灵
        wxConfigSingleton.WXConfigSingleton().robot_type = 'tl'
    elif msg['Text'] == '/关闭自动回复':
        wxConfigSingleton.WXConfigSingleton().auto_reply = False
        wxConfigSingleton.WXConfigSingleton().robot_type = ''
    elif msg['Text'] == '/使用小冰':
        wxConfigSingleton.WXConfigSingleton().auto_reply = True
        wxConfigSingleton.WXConfigSingleton().robot_type = 'xb'
    elif msg['Text'] == '/关闭小冰':
        wxConfigSingleton.WXConfigSingleton().auto_reply = False
        wxConfigSingleton.WXConfigSingleton().robot_type = ''
    elif msg['Text'] == '/使用图灵':
        wxConfigSingleton.WXConfigSingleton().auto_reply = True
        wxConfigSingleton.WXConfigSingleton().robot_type = 'tl'
    elif msg['Text'] == '/关闭图灵':
        wxConfigSingleton.WXConfigSingleton().auto_reply = False
        wxConfigSingleton.WXConfigSingleton().robot_type = ''
    elif msg['Text'] == '/开启轮询':
        itchat.send(cmd_dic[msg['Text']], toUserName='filehelper')
        # 循环
        sched.add_job(test, 'interval', seconds=5)
        # 指定日期执行
        #sched.add_job(tick, 'date', run_date='2016-02-14 15:23:05')
        '''
            job = scheduler.add_job(myfunc, 'interval', minutes=2)
            job.remove()
            # 如果有多个任务序列的话可以给每个任务设置ID号，可以根据ID号选择清除对象，且remove放到start前才有效
            sched.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
            sched.remove_job('my_job_id')
            apsched.job.Job.pause()
            apsched.schedulers.base.BaseScheduler.pause_job()
        '''
        '''
            #表示2017年3月22日17时19分07秒执行该程序
            sched.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)
 
            #表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
            sched.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
 
            #表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
            sched.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')
 
            #表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
            sched.add_job(my_job, 'cron',second = '*/5')
        '''

        try:
            sched.start()
        except:
            sched.shutdown()
    elif msg['Text'] == '/关闭轮询':
        sched.shutdown()
    itchat.send(cmd_dic[msg['Text']], toUserName='filehelper')

'''
   处理群消息
'''
def call_me_in_group(msg):
    try:
        if '台湾' in msg['Text']:
            return '台湾是中国不可分割的一部分,支持祖国收复台湾,建立台湾省'
        # 开启自动回复
        if wxConfigSingleton.WXConfigSingleton().auto_reply == True:
            if wxConfigSingleton.WXConfigSingleton().robot_type == 'tl':
                # 图灵机器人
                auto_replayOFTL(msg)
            elif wxConfigSingleton.WXConfigSingleton().robot_type == 'xb':
                global face_bug
                # 从小冰获取回复消息
                face_bug = msg['FromUserName']
                auto_replayOFXB(msg)
    except Exception as error:
        print(error)
        return

'''
   处理好友消息
'''
def call_me_in_frind(msg):
    try:
        if '台湾' in msg['Text']:
            return '台湾是中国不可分割的一部分,支持祖国收复台湾,建立台湾省'
        # 开启自动回复
        if wxConfigSingleton.WXConfigSingleton().auto_reply == True:
            if wxConfigSingleton.WXConfigSingleton().robot_type == 'tl':
                # 图灵机器人
                auto_replayOFTL(msg)
            elif wxConfigSingleton.WXConfigSingleton().robot_type == 'xb':
                global face_bug
                # 从小冰获取回复消息
                face_bug = msg['FromUserName']
                auto_replayOFXB(msg)
    except Exception as error:
        print(error)
        return

# 好友/群-文本消息
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=True)
def text_msg(msg):
    # 不是自己发送的消息，收到的信息
    if msg['FromUserName'] != wxConfigSingleton.WXConfigSingleton().my_user_name:
        # 更新聊天数据
        wxTools.updateMessage(msg_dict, msg)
        # 判断为群聊,为接收到的消息
        if '@@' in msg['FromUserName']:
            # 群中有人找小艾同学
            if wxTools.isCallMe(msg):
                call_me_in_group(msg)
        else:  # 判断为个人消息, 为接收到的消息
            call_me_in_frind(msg)
    else:
        if msg['ToUserName'] == 'filehelper':
            send_filehelper(msg)


# 好友/群-图片消息
@itchat.msg_register(itchat.content.PICTURE, isFriendChat=True, isGroupChat=True)
def image_msg(msg):
    # 不是自己发送的消息，收到的信息
    if msg['FromUserName'] != wxConfigSingleton.WXConfigSingleton().my_user_name:
        path = './images/'  # 图片路径
        imageDir = path + msg['FileName']
        # 保存文件
        if not os.path.exists(imageDir):
            wxTools.save_image_to_images(msg)
        # 更新聊天数据
        wxTools.updateMessage(msg_dict, msg)
        # 开启自动回复
        if wxConfigSingleton.WXConfigSingleton().auto_reply == True:
            try:
                # 以下方法会下载文件
                dirs = os.listdir(path)
                wxTools.sendFileMessage(type=msg['Type'], file_path=path + random.choice(dirs),to_user_name=msg['FromUserName'])
            except Exception as error:
                print(error)
                return


# 好友/群-视频消息
@itchat.msg_register([itchat.content.VIDEO], isFriendChat=True, isGroupChat=True)
def video_msg(msg):
    # 不是自己发送的消息，收到的信息
    if msg['FromUserName'] != wxConfigSingleton.WXConfigSingleton().my_user_name:
        # 保存文件
        videoDir = './videos/' + msg['FileName']
        if not os.path.exists(videoDir):
            wxTools.save_video_to_videos(msg)
        # 更新聊天数据
        wxTools.updateMessage(msg_dict, msg)
        if wxConfigSingleton.WXConfigSingleton().auto_reply == True:
            try:
                time.sleep(random.randint(1, 2))
                wxTools.sendFileMessage(type=msg['Type'], file_path=videoDir, to_user_name=msg['FromUserName'])

            except Exception as error:
                print(error)
                return

# 好友/群-文件消息
@itchat.msg_register(itchat.content.ATTACHMENT, isFriendChat=True, isGroupChat=True)
def attachment_files(msg):
    fileDir = './files/'+msg['FileName']
    # 不是自己发送的消息，收到的信息
    if msg['FromUserName'] != wxConfigSingleton.WXConfigSingleton().my_user_name:
        # 保存文件
        if not os.path.exists(fileDir):
            wxTools.save_file_to_files(msg)
        # 开启自动回复
        if wxConfigSingleton.WXConfigSingleton().auto_reply == True:
            time.sleep(random.randint(1, 2))
            wxTools.sendFileMessage(type=msg['Type'], file_path=fileDir, to_user_name=msg['FromUserName'])


'''
  收到好友邀请自动添加好友
'''
@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    #itchat.get_contract()
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
                os.remove(rev_tmp_dir + old_msg['msg_content'])
            # 删除字典旧消息
            msg_dict.pop(old_msg_id)

def test():
    wxTools.sendTextMessage(msg_text='dd', to_user_name='filehelper')

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
    sched = BlockingScheduler()
    itchat.auto_login(hotReload=True, loginCallback=after_login, exitCallback=after_logout)
    # 初始化默认配置
    initConfig()
    itchat.run(debug=True)


