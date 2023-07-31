#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, 3):
            if a > b:
                res += a ** b / i
    except Exception:
        print('Too far')
        raise
    finally:
        return res
