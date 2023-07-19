#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        sum_list = 0
        sum_weighted = 0
        for score, weight in my_list:
            sum_list += weight
            sum_weighted += score * weight
            average = sum_weighted / sum_list
        return average
