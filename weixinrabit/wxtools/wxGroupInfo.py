import itchat
'''
  根据微信号获取用户信息，返回用户信息的属性字典
  @:param user_name 用户微信账号
  user_name='@xxb096c3036543exx2d4de4fc222xxxx'
'''
def getChatRoomInfoWithGroupName(group_name):
    chat_rooms = itchat.search_chatrooms(name=group_name)
    if len(chat_rooms) > 0:
        return chat_rooms[0]


'''
  查找公众号信息
  @:param mps_name 公众号名称
  mps_name='@xxb096c3036543exx2d4de4fc222xxxx'
'''
def getMpsInfoWithGroupFromName(mps_name):
    mps_rooms = itchat.search_mps(userName=mps_name)
    if len(mps_rooms) > 0:
        return mps_rooms


'''
  查找公众号信息
  @:param mps_name 公众号名称
  mps_name='gzh'
'''
def getMpsInfoWithGroupName(mps_name):
    # itchat.search_mps(userName='@abcdefg1234567', name='gzh')
    mps_rooms = itchat.search_mps(name=mps_name)
    if len(mps_rooms) > 0:
        return mps_rooms[0]