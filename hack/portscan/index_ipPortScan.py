import subprocess
'''
 端口扫描启动程序
'''
if __name__ == '__main__':
    # subprocess.call("python3 ipPortScan.py data.txt", shell=True)
    subprocess.call("python3 ipPortScan3.py -H www.baidu.com -p 21,22,25,80,143,145,443", shell=True)