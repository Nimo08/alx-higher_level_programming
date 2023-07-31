#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        e = sys.exc_info()[1]
        sys.stderr.write("Exception: {}\n".format(str(e)))
        return False
