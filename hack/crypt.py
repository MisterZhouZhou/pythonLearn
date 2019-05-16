#!/usr/bin/python3

import _crypt

'''
cryptWord = _crypt.crypt(word, salt)
cryptWord = _crypt.crypt('egg', 'HX') => HX3232
'''

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = _crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print('[+] Found Password: ' + word + "\n")
            return
    print('[-] Password not Found.\n')
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip('\n')
            print('[*] Cracking Password For : ' + user)
            testPass(cryptPass)

if __name__ == '__main__':
  main()