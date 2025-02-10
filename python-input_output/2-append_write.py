#!/usr/bin/python3
'''
This module contains one function append_write
'''


def append_write(filename="", text=""):
    """Appends text to a file"""
    len_appended = 0
    with open(filename, 'a', encoding="utf-8") as f:
        appended_data = f.write(text)
    len_appended += len(text)
    return len_appended
