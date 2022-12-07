#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute a squared value of every member of a given matrix"""

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda x: x**2, matrix[i])))
    return new_matrix
