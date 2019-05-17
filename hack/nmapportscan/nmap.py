# from nmap import PortScanner
# pip3 install python-nmap
import optparse
import nmap

def nmapScan(tgtHost,tgtPort):
    # 创建一个PortScanner类对象
    nmScan = nmap.PortScanner()
    # 调用PortScanner类的scan()函数，将目标和端口作为参数输入并进行nmap扫描
    nmScan.scan(tgtHost, tgtPort)
    # 输出扫描结果中的状态信息
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print('[*] ' + tgtHost + " tcp/" + tgtPort + " " + state)


def main():
    parser = optparse.OptionParser("[*] Usage : ./nmapScan.py -H <target host> -p <target port[s]>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', help='specify target port[s]')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()