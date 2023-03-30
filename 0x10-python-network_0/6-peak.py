#!/usr/bin/python3
"""Technical interview preparation"""


def find_peak(list_of_integers):
    """Finds a peak (i.e. the highest value) of an
    unsorted list of integers"""

    if list_of_integers == [] or list_of_integers is None:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
