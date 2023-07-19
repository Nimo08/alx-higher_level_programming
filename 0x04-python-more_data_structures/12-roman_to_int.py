#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and \
                roman[roman_string[i]] < roman[roman_string[i+1]]:
            int_val -= roman[roman_string[i]]
        else:
            int_val += roman[roman_string[i]]
    return int_val
