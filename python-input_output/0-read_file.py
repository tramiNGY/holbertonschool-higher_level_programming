#!/usr/bin/python3
'''
This module contains one function read_files
'''


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end='')
