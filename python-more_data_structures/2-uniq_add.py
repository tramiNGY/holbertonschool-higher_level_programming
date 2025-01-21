#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(set(my_list))
    uniqadd = 0
    for i in uniq:
        uniqadd += i
    return uniqadd
