#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if 97 <= ord(i):
            res += chr(ord(i) - 32)
        else:
            res += i
    print("{:s}".format(res))
