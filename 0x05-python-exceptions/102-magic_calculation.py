#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    try:
        for i in range(94, 103):
            result += a + b
        if a > b:
            res += a ** b
    except Exception:
        print('Too far')
    finally:
        result += a / b
    return res
