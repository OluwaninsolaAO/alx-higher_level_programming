#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiply of values in a dictionary by 2"""

    new_dictionary = dict()
    for i in list(a_dictionary):
        new_dictionary[i] = a_dictionary[i] * 2

    return new_dictionary
