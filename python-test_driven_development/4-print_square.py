#!/usr/bin/python3
'''
The 4-print_squares module supplies one function print_square.
It permits to print size square of #.
size is an integer or raise TypeError and positive or raise ValueError.
'''


def print_square(size=None):
    '''
    prints a square with the character #
    '''
    if size is None:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
