#!/usr/bin/python3
"""Technical interview preparation"""


def find_peak(list_of_integers):
    """Finds a peak (i.e. the highest value) of an
    unsorted list of integers"""

    if list_of_integers == [] or list_of_integers is None:
        return None
    # if len(list_of_integers) == 2:
        # return max(list_of_integers)
    # if len(list_of_integers) == 3:
        # if list_of_integers[1] == max(list_of_integers):
        #   return list_of_integers[1]
        # return None

    # mid = len(list_of_integers) // 2
    # left = find_peak(list_of_integers[:mid])
    # right = find_peak(list_of_integers[mid:])
    # if left is None:
        # return right
    # if right is None:
        # return left
    # if left > right:
        # return left
    # return right

    list_of_integers.sort()
    return list_of_integers[-1]
