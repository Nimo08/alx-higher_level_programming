#!/usr/bin/python3
def remove_char_at(str, n):
    x = str[:n]
    y = str[n + 1:]
    return x + y
