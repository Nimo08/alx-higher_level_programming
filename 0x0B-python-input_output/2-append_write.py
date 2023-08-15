#!/usr/bin/python3
def append_write(filename="", text=""):
    filename = "file_append.txt"
    text = "This School is so cool!\n"
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
