#!/usr/bin/python3
"""
This module contains a class definition Base with the
following attributes:
    - private class attribute __nb_objects = 0 for a
    start.
"""
import json


class Base:
    """
    ``Base`` will have a class attribute ``__nb_objects``
    with its constructor taking the arguement ``id``
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for the class Base.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of
        ``list_dictionaries``.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
