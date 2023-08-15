#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""
Imports json and sys modules, as well as save_to_json_file
and load_from_json file.
Adds all arguments to a Python list, and then save them to
a file.
"""
arg = sys.argv
filename = "add_item.json"
with open(filename, 'a+', encoding="utf-8") as f:
    arg_list = []
    arg_list += arg[1:]
    save_to_json_file(arg_list, filename)
    load_from_json_file(filename)
