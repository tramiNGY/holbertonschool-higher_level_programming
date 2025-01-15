#!/usr/bin/python3
def uppercase(str):
    upperstring = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            upperstring += chr(ord(i) - 32)
        else:
            upperstring += i
    print(upperstring)
    return (upperstring)
