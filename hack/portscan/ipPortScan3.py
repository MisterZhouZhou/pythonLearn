import optparse
import socket
import threading

'''
 端口扫描
'''

#定义一个信号量
screenLock = threading.Semaphore(value=1)

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        result = connSkt.recv(1024)
        # 执行一个加锁操作
        screenLock.acquire()
        print('[+] %d/tcp open' % tgtPort)
        print('[+] ' + str(result))
    except Exception as e:
        # 执行一个加锁操作
        screenLock.acquire()
        print('[-] %d/tcp closed' % tgtPort)
    finally:
        # 执行释放锁操作， 同时将socket关闭
        screenLock.release()
        connSkt.close()


def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)  # 获取主机地址
    except:
        print("[-] Cannot resolve '%s' : Unknown host" % tgtHost)

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)

    # 设置socket超时
    socket.setdefaulttimeout(5)
    for tgtPort in tgtPorts:
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser("[*] Usage : ./portscanner.py -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s]')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()