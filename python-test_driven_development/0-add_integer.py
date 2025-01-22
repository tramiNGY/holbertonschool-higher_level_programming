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
        if a != a:
            raise ValueError("cannot convert float NaN to integer")
        if a < -1.7976931348623157e+308 or a > 1.7976931348623157e+308:
            raise OverflowError("cannot convert float infinity to integer")
        else:
            a = int(a)
    if isinstance(b, float):
        if b != b:
            raise ValueError("cannot convert float NaN to integer")
        if b < -1.7976931348623157e+308 or b > 1.7976931348623157e+308:
            raise OverflowError("cannot convert float infinity to integer")
        else:
            b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
