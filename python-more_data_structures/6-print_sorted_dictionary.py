#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    for i in range(len(keys)):
        print("{}: {}".format(keys[i], a_dictionary[keys[i]]))
