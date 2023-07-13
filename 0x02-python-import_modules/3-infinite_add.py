#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = len(argv)
    res = 0
    for i in range(1, arg):
        res += int(argv[i])
    print("{:d}".format(res))
