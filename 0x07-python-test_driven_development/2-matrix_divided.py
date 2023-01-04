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

    if type(matrix) != list:
        raise TypeError(msg1)
    else:
        try:
            type(matrix[0])
        except IndexError:
            raise TypeError(msg1)

        for i in range(len(matrix)):
            try:
                type(matrix[i])
            except IndexError:
                raise TypeError(msg1)
            if type(matrix[i]) != list:
                raise TypeError(msg1)
            elif len(matrix[i]) == 0:
                raise TypeError(msg1)

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
