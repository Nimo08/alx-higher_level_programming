#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        my_list = []

    list_set = set(my_list)
    uniq_list = list(list_set)
    uniq_sum = sum(uniq_list)
    return uniq_sum
