# /usr/local/bin/python3
import time
import bluetooth
alreadyFound = []

def findDevs():
    try:
        foundDevs = bluetooth.discover_devices(lookup_names = True)
    except bluetooth.BluetoothError as e:
        print(e)
        return None
    for (addr, name) in foundDevs:
        if addr not in alreadyFound:
            print("[*] Found Bluetooth Device :  " + str(name))
            print("[+] MAC address :  " + str(addr))
            alreadyFound.append(addr)

def connect():
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect(('C0:CC:F8:D9:F4:A9', 1))
    command = "/%d;" % 11
    print("Sending command (%s)" % command)
    sock.send(command.encode('utf-8'))
    sock.settimeout(2)
    response = ""
    try:
        while True:
            r = sock.recv(255)
            if not r:
                break
            response = response + r
            if r.find(";") != -1:  # we have reach end of message
                break
    except:
        pass
    print("Response: (%s)" % response)
    # sock.close()

if __name__ == '__main__':
    # findDevs()
    # connect()
    service = bluetooth.find_service(address= 'C0:CC:F8:D9:F4:A9')
    print(service)

    # while True:
        # findDevs()
        # time.sleep(5)