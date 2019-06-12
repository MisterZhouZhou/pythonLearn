from weixinrabit.models import User
import itchat

'''
  获取自己的用户信息，返回自己的属性字典
'''
def getUserInfoOfMe():
    result = itchat.search_friends()
    user_name = result['UserName']
    return User(
        user_name=user_name
    ) if user_name else None

'''
  是否为自己发送的消息
'''
def isSendMsgOfMe(from_user_name):
    mySelf = getUserInfoOfMe()
    if not from_user_name == mySelf.user_name:  # 不是自己发送的消息
        return True
    return False


'''
  根据用户昵称获取用户信息，返回用户信息的属性字典
  @:param nick_name 用户昵称
'''
def getFriendWithNickName(nick_name):
    result = itchat.search_friends(name=nick_name)
    user_name = result[0]['UserName']
    return User(
        user_name=user_name
    ) if user_name else None


'''
  根据微信号获取用户信息，返回用户信息的属性字典
  @:param wx_account 用户微信账号
'''
def getFriendWithAccount(wx_account):
    result = itchat.search_friends(wechatAccount=wx_account)
    user_name = result['UserName']
    return User(
        user_name=user_name,
        nick_name=result['NickName']
    ) if user_name else None


'''
  根据微信号获取用户信息，返回用户信息的属性字典
  @:param user_name 用户微信账号
  user_name='@xxb096c3036543exx2d4de4fc222xxxx'
'''
def getFriendWithUserName(user_name):
    if user_name.find('@@') != -1:
        user_name = '@' + user_name.split('@@')[1]
    result = itchat.search_friends(userName=user_name)
    return User(
        user_name=result['UserName'],
        nick_name=result['NickName']
    ) if result else None