#!/usr/bin/python3
"""
This programme prints sqaure with
the character '#'
"""


def print_square(size):
    """
    ``size``: The size of the square (required)
                - size must be an integer
                - size must be greater than or equals 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
