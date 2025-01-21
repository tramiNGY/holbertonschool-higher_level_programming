#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    decimal_number = 0
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        current_value = roman_numerals[roman_string[i]]
        if i + 1 < len(roman_string):
            next_value = roman_numerals[roman_string[i+1]]
            if current_value < next_value:
                decimal_number -= current_value
            else:
                decimal_number += current_value
        else:
            decimal_number += current_value
    return decimal_number
