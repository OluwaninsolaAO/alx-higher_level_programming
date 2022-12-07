#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds a series of unique number from a list"""

    result = 0
    for i in set(my_list): result += i
    return result
