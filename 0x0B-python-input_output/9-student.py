#!/usr/bin/python3
"""
A class that defines a student by
- first_name
- last_name
- age
"""


class Student:
    """
    All member of the class will be having a
    public method ``to_json()`` which will return
    a dictionary representation of the member of
    the class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the class Student with the
        following attributes, expected to be defined:
        - first_name
        - last_name
        - age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the
        member of the class.
        """
        return self.__dict__
