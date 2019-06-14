import itchat
from weixinrabit.models import Group
'''
  根据微信群名称获取微信群信息
  @:param group_name 微信群名称
  group_name='1xx1'
  
  groupInfo = wxGroupInfo.getGroupInfoWithGroupName('呵呵')
  itchat.send_msg("dd", toUserName=groupInfo.user_name)
'''
def getGroupInfoWithGroupName(group_name):
    chat_rooms = itchat.search_chatrooms(name=group_name)
    if len(chat_rooms) > 0:
        user_name = chat_rooms[0]['UserName']
        nick_name = chat_rooms[0]['NickName']
        return Group(
            user_name=user_name,
            nick_name=nick_name
        ) if user_name else None


'''
  根据微信群名称获取微信群信息
  @:param group_name 微信群名称
  group_id='@ddd1xx1'
'''


def getGroupInfoWithGroupId(group_id):
    chat_rooms = itchat.search_chatrooms(userName=group_id)
    if len(chat_rooms) > 0:
        user_name = chat_rooms['UserName']
        nick_name = chat_rooms['NickName']
        return Group(
            user_name=user_name,
            nick_name=nick_name
        ) if user_name else None


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