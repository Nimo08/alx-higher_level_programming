#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        if a > b:
            raise Exception
            print('Too far')
        else:
            res += a ** b / i
        return res
