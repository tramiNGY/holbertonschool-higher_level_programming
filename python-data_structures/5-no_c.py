#!/usr/bin/python3
def no_c(my_string):
    list_removed = []
    for i in my_string:
        if i != 'c' and i != 'C':
            list_removed.append(i)
    return ''.join(list_removed)
