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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of
        ``list_dictionaries``.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of
        ``list_objs`` to a file:
        - ``list_objs`` is a list if instances who inherits of Base
        - The file name will be <class name>.json
        - Overwrite the file if it already exists.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fi:
            if list_objs is None:
                fi.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                fi.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns python data structure of ``json_string`` arguement
        passed into the method:
        - ``json_string`` being a json string representation
        of dictionaries.
        - if ``json_string`` is None or empty, the method returns
        an empty list otherwise, return the list represented by
        ``json_string``.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

