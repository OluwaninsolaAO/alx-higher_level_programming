#!/usr/bin/python3
"""
A simple pythong programme that divides all elements of
a matrix by a ``div`` and return the new list.
"""


def matrix_divided(matrix, div):
    """
    Compute a division of the elements in ``matrix``
    using ``div`` and returning the resulting new
    matrix.
    """
    types = [int, float]
    lenght = -1

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"

    for i in matrix:
        for j in i:
            if type(j) not in types:
                raise TypeError(msg1)
        if lenght != -1:
            if lenght != len(i):
                raise TypeError(msg2)
        lenght = len(i)
    if type(div) not in types:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(round(j / div, 2))
        result.append(temp)
    return result
