#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_replaced = my_list[:]
    if idx < 0:
        return my_list_replaced
    if idx > len(my_list) - 1:
        return my_list_replaced
    my_list_replaced[idx] = element
    return my_list_replaced
