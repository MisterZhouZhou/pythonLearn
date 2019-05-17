import optparse
import socket

'''
 端口扫描
'''

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        result = connSkt.recv(1024)
        print('[+] %d/tcp open' % tgtPort)
        print('[+] ' + str(result))
        connSkt.close()
    except Exception as e:
        print('[-] %d/tcp closed' % tgtPort)

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
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))


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