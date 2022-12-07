#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print sorted dictionary"""

    for x in sorted(a_dictionary):
        print("{} : {}".format(x, a_dictionary[x]))
