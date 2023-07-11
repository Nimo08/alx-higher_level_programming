#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i == 102 - 1):
            print("{:d}".format(i), end="")
        elif (i % 15 == 0):
            print("{:s}".format("Fizz Buzz"), end=" ")
        elif (i % 3 == 0):
            print("{:s}".format("Fizz"), end=" ")
        elif (i % 5 == 0):
            print("{:s}".format("Buzz"), end=" ")
        else:
            print("{:d}".format(i), end=" ")
