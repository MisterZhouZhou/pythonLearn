from serial.tools import list_ports
import serial

if __name__ == '__main__':
    plist = list(list_ports.comports())
    if len(plist) <= 0:
        print('没有发现端口!')
    else:
        for i in range(0, len(plist)):
            print(plist[i])
        # plist_0 = list(plist[0])
        # serialName = plist_0[0]
        # serialFd = serial.Serial(serialName, 9600, timeout=60)
        # print("可用端口名>>>", serialFd.name)

# if __name__ == '__main__':
#     serial = serial.Serial('/dev/ttyS0', 115200)
#     print(serial)
#     if serial.isOpen():
#        print("open success")
#     else:
#         print("open failed")
