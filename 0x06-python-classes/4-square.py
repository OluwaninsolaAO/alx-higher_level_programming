#!/usr/bin/python3
"""Defines a class Square with  its various properties"""


class Square:
    """Just a square class, with all its awesome
    fields and attributes"""

    def __init__(self, size=0):
        """Object/Instance Initial Setup"""
        self.__size = size

    def area(self):
        """Computes the area of a square using ``__size``"""
        return self.__size * self.__size

    @property
    def size(self):
        """A getter for instance attribute size
        Returns the value of ``__size``"""
        return self.__size

    @size.setter
    def size(self, size):
        """A setter for instance attribute size
        Sets a value for ``__size``"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
