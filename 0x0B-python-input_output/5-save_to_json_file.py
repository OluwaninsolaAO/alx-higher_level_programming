#!/usr/bin/python3
"""
A simple programm that writes an Object to a text
file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    ``my_obj`` being the python data structure to
    be serialized and ``filename`` is the filename
    the JSON string going to be written into.
    This function returns nothing.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
