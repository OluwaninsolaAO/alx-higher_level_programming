#!/usr/bin/python3
"""
A simple class extended from another class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square being an extension or a
    sub-class of Rectangle
    """
    def __init__(self, size):
        """instantiation of the member of the class"""
        super().integer_validator("size", size)
        super().__init__(size, size)
