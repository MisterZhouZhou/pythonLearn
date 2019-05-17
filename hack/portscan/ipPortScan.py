import socket, os, sys

'''
 端口扫描
'''

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        print(str(e))
        return


def checkVulns(banner):
    if 'vsFTPd' in banner:
        print('[+] vsFTPd is vulnerable.')
    elif 'FreeFloat Ftp Server' in banner:
        print('[+] FreeFloat Ftp Server is vulnerable.')
    elif 'pyftpdlib' in banner:
        print('[+] pyftpdlib Ftp Server is vulnerable.')
    else:
        print('[-] FTP Server is not vulnerable.')
    return


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] ' + filename + ' does not exit.')
            exit(0)

        if not os.access(filename, os.R_OK):
            print('[-] ' + filename + ' access denied.')
            exit(0)

        print('[+] Reading From: ' + filename)
    else:
        print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
        exit(0)

    portList = [21, 22, 25, 80, 110, 443]
    ip = '10.10.10.128'
    for port in portList:
        banner = retBanner(ip, port)
        if banner:
            print('[+] ' + ip + ':' + str(port) + '--' + banner)
            if port == 21:
                checkVulns(banner, filename)

if __name__ == '__main__':
    main()