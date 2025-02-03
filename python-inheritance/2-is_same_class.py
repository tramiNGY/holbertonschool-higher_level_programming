#!/usr/bin/python3
'''
This module contains one function is_same_class
'''


def is_same_class(obj, a_class):
    '''
    Checks if obj is exactly of a_class
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
