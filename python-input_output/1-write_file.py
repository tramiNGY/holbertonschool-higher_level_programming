#!/usr/bin/python3
'''
This module contains one function write_file
'''


def write_file(filename="", text=""):
    """Open and write text in file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
