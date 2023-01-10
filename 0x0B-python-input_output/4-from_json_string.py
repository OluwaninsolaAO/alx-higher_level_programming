#!/usr/bin/python3
"""
A programme that returns an object (Python
data structure) represnetated by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    ``my_str`` being a JSON String object to be
    converted back to a pyhton data structure.
    Returns a Python Data Structure represented
    by the JSON String ``my_str``.
    """
    return json.loads(my_str)
