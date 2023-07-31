#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        num = a / b
    except ZeroDivisionError:
        num = None
        return None
    finally:
        print("Inside result: {}".format(num))
    return num
