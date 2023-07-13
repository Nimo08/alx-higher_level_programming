#!/usr/bin/python3
def magic_calculation(a, b):
    from calculator_1 import add, sub
    if a < b:
        c = add(a, b)
    for i in range(38, 90):
        c = add(a, b)
        sub(a, b)
