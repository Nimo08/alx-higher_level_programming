#!/usr/bin/python3
for i in range(1, 90):
    if (i == 90 - 1):
        print("{:02d}".format(i), end=" \n")
    else:
        print("{:02d}".format(i), end=", ")
