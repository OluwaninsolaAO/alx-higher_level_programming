#!/usr/bin/python3
"""Defines a class Square with  its various properties"""


class Square:
    """Just a square class, with all its awesome
    fields and attributes"""

    def __init__(self, size=0):
        """Object/Instance Initial Setup"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
