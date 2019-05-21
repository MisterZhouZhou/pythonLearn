from scapy.all import srp
from scapy.layers.l2 import Ether, ARP

ipScan = '192.168.0.1/24'
try:
    ans, unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ipScan), timeout=2)
except Exception as e:
    print(e)
else:
    for send, rcv in ans:
        ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")
        print(ListMACAddr)