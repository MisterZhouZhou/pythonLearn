'''
  配置单利
'''

def SingleTon(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@SingleTon
class WXConfigSingleton(object):
    # 自动登录
    auto_reply = False
    # 自己的id
    my_user_name = ''

