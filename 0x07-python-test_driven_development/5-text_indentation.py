#!/usr/bin/python3
"""
Module contains text_indentation function
text_indentation function: Prints a text with 2
new lines after each of these characters: .?:
TypeError occurs when the text is not a string
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: string
    Return: text with 2 new lines after: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    idx = 0
    delim = [".", ":", "?"]
    for char in text:
        if char in (delim):
            line += char
            line += "\n\n"
            while idx < len(line) and line[idx] == " ":
                idx += 1
            print(line[idx:], end="")
            idx = 0
            line = ""
        else:
            line += char
    if line:
        while idx < len(line) and line[idx] == " ":
            idx += 1
        print(line[idx:], end="")
        idx = 0
        line = ""
