#!/usr/bin/python3
def uppercase(str):
    print(''.join([chr(ord(i) - 32) if 97 <= ord(i) <= 122
                   else i for i in str]))
