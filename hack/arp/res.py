from scapy.all import *
from scapy.layers.l2 import ARP

# 查询局域网中主机mac地址
res = sr1(ARP(pdst='192.168.1.60'))
print(res)