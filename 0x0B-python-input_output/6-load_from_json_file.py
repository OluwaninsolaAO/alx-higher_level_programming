#!/usr/bin/python3
"""
A simple programme that creates an
Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    ``filename`` being the name or the directory
    where the JSON string is located.
    The function simply creates and Return the
    object created from the JSON string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
