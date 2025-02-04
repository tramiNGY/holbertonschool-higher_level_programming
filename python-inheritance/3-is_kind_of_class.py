#!/usr/bin/python3
'''
This module contains one function is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''
    Checks if obj is an instance of or inherited class
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
