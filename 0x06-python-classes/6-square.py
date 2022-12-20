#!/usr/bin/python3
"""Defines a class Square with  its various properties"""


class Square:
    """Just a square class, with all its awesome
    fields and attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Object/Instance Initial Setup"""
        self.__size = size
        self.__position = position

    def area(self):
        """Computes the area of a square using ``__size``"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square using #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                a, b = self.__position
                for m in range(a):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end="")
                print("")

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

    @property
    def position(self):
        """A getter for instance attribute position
        Returns the value of ``__position``"""
        return self.__position

    @position.setter
    def position(self, value):
        """A setter for instance attribbute position
        Sets a value for ``__position``"""
        if type(value) is tuple and len(value) == 2:
            a, b = value
            if (type(a) != int) or (type(b) != int):
                raise TypeError("position must be a tuple\
                                of 2 positive integers")
        else:
            raise TypeError("position must be a tuple\
                            of 2 positive integers")
        self.__position = value
