#!/usr/bin/python3.6.5

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or more recent version is required.")

max_key_size = 26

def getMode():
    while True:
        print ("Do you wish to encrypt or decrypt a message?")
        mode = input().lower()
        
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd'.")

def getMessage():
    print ("Enter your message: ")
    return input()

def getKey():
    key = ()

    while True:
        print ("Enter the key number (1-%s" % (max_key_size))
        key = int(input())
        
        if(key >= 1 and key <= max_key_size):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print ("Your translated text is: ")
print (getTranslatedMessage(mode,message,key))

