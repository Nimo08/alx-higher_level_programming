#!/usr/bin/python3
def print_last_digit(number):
    num = int(str(number)[-1])
    if (num > 0):
        print("{:d}".format(num), end="")
    elif (num < 0):
        num = num * -1
        print("{:d}".format(num), end="")
    else:
        print("{:d}".format(0), end="")
    return num
