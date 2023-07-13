#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = len(argv)
    if arg == 1:
        print(arg - 1, "arguments.")
    elif arg == 2:
        print(arg - 1, "argument:")
        for i in range(1, arg):
            print("{:d}: {:s}".format(i, argv[i]))
    else:
        print(arg - 1, "arguments:")
        for i in range(1, arg):
            print("{:d}: {:s}".format(i, argv[i]))
