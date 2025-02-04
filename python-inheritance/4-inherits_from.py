#!/usr/bin/python3
'''
This module contains one function inherits_from
'''


def inherits_from(obj, a_class):
    '''
    Checks if obj an inherited class
    '''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
