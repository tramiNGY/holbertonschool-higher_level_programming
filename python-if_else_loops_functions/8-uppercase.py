#!/usr/bin/python3
def uppercase(str):
    upperstring = []
    for i in str:
        if 97 <= ord(i) <= 122:
            upperstring.append(chr(ord(i) - 32))
        else:
            upperstring.append(i)
    print(''.join(upperstring))
