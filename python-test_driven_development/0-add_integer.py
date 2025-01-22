#!/usr/bin/python3
'''
The 0-add_integer module supplies one function add_integer().
It permits to add two integers.
If float types are inputed, it converts it to integers.
'''


def add_integer(a, b=98):
    '''
    Adds a and b if integers otherwise raises error
    '''
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
