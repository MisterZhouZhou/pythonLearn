#coding:utf-8
import socket, threading, time
'''
 服务端socket
'''

def dealClient(socket, addr):
    # 第四步： 接收传来的数据， 并发送给对方数据
    print('Accept new connection from %s:%s...' % addr)
    socket.send(b'Hello, I am server1')
    while True:
        data = socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('-->%s!' % data.decode('utf-8'))
        socket.send(('Loop_Msg:%s!' % data.decode('utf-8')).encode('utf-8'))
    # 第五步：关闭socket
    socket.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    # 第一步：创建一个基于ipv4和TCP协议的socket
    # Socket 绑定的IP（127.0.0.1)与端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    # 第二步：监听连接
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 第三步： 接收一个新的连接
        socket, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=dealClient, args=(socket, addr))
        t.start()