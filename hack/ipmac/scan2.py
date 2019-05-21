from scapy.all import *
from scapy.layers.l2 import Ether, ARP

def main():
        for ipFix in range(1, 254):
            ip = "192.168.0." + str(ipFix)
            arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
            res = srp1(arpPkt, timeout=1, verbose=0)
            if res:
                print("IP: " + res.psrc + "     MAC: " + res.hwsrc)

if __name__ == "__main__":
        main()