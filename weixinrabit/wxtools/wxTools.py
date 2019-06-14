'''
  是否有人@自己
'''
def isAtMe(msg):
    return msg['isAt']


'''
  是否有人提到小艾
'''
def isCallMe(msg):
    if isAtMe(msg) or msg['Text'].find('小艾') != -1:
        return True
    else:
        return False


'''
  是否有人提到小艾
'''
def sendTextMessage(msg_text, to_user_name):
    import itchat
    """
        如果单纯的使用send函数，需要对发送内容进行标注。
        @fil@：在发送内容前添加，表明是发送文件
        @img@：在发送内容前添加，表明是图片文件
        @msg@：在发送内容前添加，表明是消息
        @vid@：在发送内容前添加，表明是视频文件，视频文件要小于20M
        如果什么都没有添加，默认是消息
    """
    itchat.send(msg_text, toUserName=to_user_name)

'''
  发送文件/图片/视频消息
  @:param type:  Picture, Video
'''
def sendFileMessage(type, to_user_name=None, file_path=None):
    import time, random, itchat
    typeSymbol = {'Picture': 'img', 'Video': 'vid'}.get(type, 'fil')
    reply = '@%s@%s' % (typeSymbol, file_path)
    if to_user_name == None:
        return reply
    if to_user_name.find('@@') != -1:
        to_user_name = '@' + to_user_name.split('@@')[1]
    # 发送消息
    time.sleep(random.randint(1, 2))
    itchat.send(reply, toUserName=to_user_name)


'''
  保存图片
'''
def save_image_to_images(msg):
    path = './images/'  # 图片路径
    # 保存的会有一样的图片。。。
    msg['Text'](path+msg['FileName'])

'''
  保存文件
'''
def save_file_to_files(msg):
    path = './files/'  # 图片路径
    # 保存的会有一样的图片。。。
    msg['Text'](path+msg['FileName'])

'''
  保存文件
'''
def save_video_to_videos(msg):
    path = './videos/'  # 图片路径
    # 保存的会有一样的图片。。。
    msg['Text'](path+msg['FileName'])



'''
  更新消息数据
'''
def updateMessage(msg_dict, msg):
    import time, itchat, re, os
    from weixinrabit.wxtools import wxUserInfo
    # 获取的是本地时间戳并格式化本地时间戳 e: 2019-02-16 13:43:20
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 消息ID
    msg_id = msg['MsgId']
    # 消息时间
    msg_time = msg['CreateTime']
    msg_friend = wxUserInfo.getFriendWithUserName(msg['FromUserName'])
    msg_from =  ''
    if (msg_friend != None):
        msg_from = msg_friend.nick_name
    # 消息内容
    msg_content = None
    # 分享的链接
    msg_share_url = None
    if msg['Type'] == 'Text' \
            or msg['Type'] == 'Friends':
        msg_content = msg['Text']
    elif msg['Type'] == 'Recording' \
            or msg['Type'] == 'Attachment' \
            or msg['Type'] == 'Video' \
            or msg['Type'] == 'Picture':
        msg_content = r"" + msg['FileName']
        # 保存文件
        msg['Text']("./temps/" + msg['FileName'])
    elif msg['Type'] == 'Card':
        msg_content = msg['RecommendInfo']['NickName'] + r" 的名片"
    elif msg['Type'] == 'Map':
        x, y, location = re.search(
            "<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()
        else:
            msg_content = r"" + location
    elif msg['Type'] == 'Sharing':
        msg_content = msg['Text']
        msg_share_url = msg['Url']
    # 更新字典
    msg_dict.update(
        {
            msg_id: {
                "msg_from": msg_from, "msg_time": msg_time, "msg_time_rec": msg_time_rec,
                "msg_type": msg["Type"],
                "msg_content": msg_content, "msg_share_url": msg_share_url
            }
        }
    )


'''
  初始化缓存目录
'''
def initTempConfig():
    import os
    rev_tmp_dir = "./temps/"
    if not os.path.exists(rev_tmp_dir):
        os.makedirs(rev_tmp_dir)

'''
 移除缓存目录
 '''
def removeTempConfig():
    import os, shutil
    rev_tmp_dir = "./temps/"
    if os.path.exists(rev_tmp_dir):
        shutil.rmtree(rev_tmp_dir)