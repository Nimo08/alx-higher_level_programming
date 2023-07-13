#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arg = len(sys.argv)
    if arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
        sys.exit(0)
    elif op == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
        sys.exit(0)
    elif op == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
        sys.exit(0)
    elif op == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
