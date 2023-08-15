#!/usr/bin/python3
"""
Imports sys module, save_to_json_file
and load_from_json file.
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    """
    Adds all arguments to a Python list, and then save them to
    a file.
    """
    filename = "add_item.json"
    with open(filename, 'a+', encoding="utf-8") as f:
        args = sys.argv[1:]
        args_list = []
        if filename:
            args_list = load_from_json_file(filename)
        else:
            args_list = []
        args_list.extend(args)
        save_to_json_file(args_list, filename)
