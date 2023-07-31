#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        sys.stderr.write("Exception: Unknown format code 'd'")
        sys.stderr.write("for object of type 'str'\n")
        return False
