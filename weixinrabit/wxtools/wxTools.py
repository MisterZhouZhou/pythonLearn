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
  保存图片
'''
def saveImageToImages(msg):
    path = './images/'  # 图片路径
    # 保存的会有一样的图片。。。
    msg['Text'](path+msg['FileName'])


'''
  更新消息数据
'''
def updateMessage(msg_dict, msg):
    import time, itchat, re, os
    # 获取的是本地时间戳并格式化本地时间戳 e: 2019-02-16 13:43:20
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 消息ID
    msg_id = msg['MsgId']
    # 消息时间
    msg_time = msg['CreateTime']
    msg_from = (itchat.search_friends(userName=msg['FromUserName']))["NickName"]
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
        msg['Text'](os.getcwd() + "/temps/" + msg['FileName'])
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
