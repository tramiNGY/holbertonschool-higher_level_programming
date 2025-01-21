#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    number_printed = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
            number_printed += 1
        except IndexError:
            break
        except ValueError:
            print("Could not convert data to an integer", end="")
            i += 1
    print()
    return number_printed
