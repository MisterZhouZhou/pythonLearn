import zipfile
import optparse
from threading import Thread
'''
 一个Zip文件口令破解机
 optparse模块主要用来为脚本传递命令参数功能.
 
'''

'''
  压缩文件密码尝试破解
'''
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print('[+] Fonud Password : ' + password + '\n')
    except Exception as e:
        print(e)
        pass


def main():
    parser = optparse.OptionParser("[*] Usage: ./unzip.py -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    zFile = zipfile.ZipFile(options.zname)
    passFile = open(options.dname)
    for line in passFile.readlines():
        line = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, line))
        t.start()

if __name__ == '__main__':
	main()