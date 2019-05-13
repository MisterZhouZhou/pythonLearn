# coding:utf-8

class ProxyInfo(object):
    def __init__(self, **kwargs):
        self.ip = kwargs.get('ip')  # ip
        self.port = kwargs.get('port')  # 端口
        self.type = kwargs.get('type')