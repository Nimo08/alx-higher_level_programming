#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        sys.stderr.flush()
        return None
