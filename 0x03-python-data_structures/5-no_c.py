#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    else:
        for i in my_string:
            return my_string.translate({ord('c'): None, ord('C'): None})
