#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = 10 - number % 10
    print(last_digit, end='')
    return (last_digit)
