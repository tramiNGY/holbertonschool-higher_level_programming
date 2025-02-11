#!/usr/bin/python3
'''
This module contains one function pascal_triangle
'''


def pascal_triangle(n):
    mainlist = []
    sublist = []
    if n <= 0:
        return mainlist
    for line in range(n):
        sublist = [1] * (line + 1)
        for column in range(1, line):
            sublist[column] = (mainlist[line - 1][column - 1] +
                               mainlist[line - 1][column])
        mainlist.append(sublist)
    return mainlist
