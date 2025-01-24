#!/usr/bin/python3
'''
The 3-say_my_name module supplies one function say_my_name.
It permits to print "My name is <first name> <last_name>"
It should permit to print only one name is the other ommited.
'''


def say_my_name(first_name, last_name=""):
    '''
    Prints the first name and last name
    '''
    if first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
