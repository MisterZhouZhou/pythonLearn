import subprocess

if __name__ == '__main__':
    subprocess.call("python3 nmap.py -H www.baidu.com -p 21,22,25,80,143,145,443", shell=True)