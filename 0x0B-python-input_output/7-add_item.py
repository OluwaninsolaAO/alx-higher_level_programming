#!/usr/bin/python3
"""
A simple programme that adds all arguements to a Python
list, and the save them to a file.
Everytime the programme is called, arguements passed to
the programme will be append at the end.
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    filename = "add_item.json"

    try:
        obj = load_from_json_file(filename)
    except FileNotFoundError:
        obj = []
    obj.extend(sys.argv[1:])
    save_to_json_file(obj, filename)
