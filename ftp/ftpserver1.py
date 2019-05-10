# 方法一：SimpleHTTPServer
'''
$ cd /home/haoel
$ python -m SimpleHTTPServer
$ python -m SimpleHTTPServer 8080
'''

# python3 中``被放到了http.server中，启动方式变成
'''
python3 -m http.server 9090
'''

#  访问地址：
'''
http://192.168.1.1:8000
'''



# 方法二：自定义ftp服务
# 定制HTTP服务器只能服务于本地环境
# 定制信息如下
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_ftp():
    handlerClass = SimpleHTTPRequestHandler
    protocol = 'HTTP/1.0'

    # 配置端口号
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 9000
    server_address = ('127.0.0.1', port)

    # 配置服务
    handlerClass.protocol_version = protocol
    httpd = HTTPServer(server_address, handlerClass)
    # 获取socket服务信息
    sa = httpd.socket.getsockname()
    print('Servering HTTP on', sa[0], 'port', sa[1], '...')
    # 启动服务
    httpd.serve_forever()

if __name__ == '__main__':
    run_ftp()


