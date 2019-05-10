# coding:utf-8
# 使用ftplib库开启ftp服务

from pyftpdlib.authorizers import DummyAuthorizer  # 授权
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp():
    # 新建一个用户组
    authorizer = DummyAuthorizer()
    # 将用户名、密码、指定目录、权限添加到里面
    authorizer.add_user('fan', 'root', '/Users/zhouwei/Desktop/', perm='elr') #elradfmwM #adfmw
    # 这个是添加匿名用户,任何人都可以访问，如果去掉的话，需要输入用户名和密码，可以自己尝试
    authorizer.add_anonymous("/Users/zhouwei/Desktop/love/")

    handler = FTPHandler
    handler.authorizer = authorizer
    # 开启服务器
    server = FTPServer(('127.0.0.1', 9000), handler)
    server.serve_forever()

if __name__ == '__main__':
    run_ftp()

'''
查看
ftp://localhost:9000/
'''