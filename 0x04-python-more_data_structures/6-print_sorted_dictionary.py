#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = sorted(a_dictionary.keys())
    for key in res:
        print(key, ':', a_dictionary[key])
