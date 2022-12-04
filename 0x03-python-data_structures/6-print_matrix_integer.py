#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][col]), end="")
        print()
