#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for i in my_list:
        if i > idx:
            return None
        else:
            return my_list[idx]
