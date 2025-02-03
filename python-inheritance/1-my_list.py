#!/usr/bin/python3
'''
This module contains one class list with its subclass MyList
'''


class MyList(list):
    """This is a subclass of list"""
    def print_sorted(self):
        print(sorted(self))